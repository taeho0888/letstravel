from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import User
import json
import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_answer(question):
    prompt = f"""
    안녕 나는 여행 코스 추천 회사의 매니저야. 
    너에게 여행 코스 추천을 도움 받으려고 해. 
    내가 유저의 여행 관련 정보들을 제시해줄테니 여행 코스를 짜줘. 
    여기는 대한민국이고 언급이 굳이 없으면 해외 여행지를 추천해줘도 좋아. 
    경비는 인당 기준으로 생각해줘~

    시기: {question.get('month')}
    날짜: {question.get('duration')}
    여행 희망 지역 : {question.get('where')}
    여행 경비: 인당 {question.get('budget')}
    여행 키워드: {question.get('keyword')}
    여행 목적: {question.get('purpose')}
    여행 동반자: {question.get('accompany')}

    추천 코스의 경비의 합은 유저가 준 여행 경비를 넘으면 안돼.
    대답은 일자별로 정리해서 시간마다 형태로 대답해줘.
    """
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": prompt
        }],
        stream=True,
    )
    content = completion["choices"][0].get("delta", {}).get("content")
    if content is not None:
        return content
        

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        print(text_data)
        id = json.loads(text_data)
        user = User.objects.get(id=id)
        question = {}
        question['month'] = user.month
        question['duration'] = user.duration
        question['where'] = user.where
        question['budget'] = user.budget
        question['keyword'] = user.keyword
        question['accompany'] = user.accompany
        answer = await generate_answer(question)
        user.answer = answer
        await sync_to_async(user.save)()
        await self.send(text_data=json.dumps({'answer': answer}))
