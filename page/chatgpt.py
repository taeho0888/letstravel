import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatBot:

    def make_question(self, question):
        json = '''
        {
            "일차": {
                "시간": {
                    "장소" : 
                    "활동" :
                    "예상경비" :
                }
            }
        }
        '''

        return f"""
        안녕 나는 여행 코스 추천 회사의 매니저야. 
        너에게 여행 코스 추천을 도움 받으려고 해. 
        내가 유저의 여행 관련 정보들을 제시해줄테니 여행 코스를 짜줘. 
        여기는 대한민국이고 언급이 굳이 없으면 해외 여행지를 추천해줘도 좋아. 
        경비는 인당 기준으로 생각해줘~

        시기: {question['month']}
        날짜: {question['duration']}
        여행 경비: 인당 {question['budget']}
        여행 키워드: {question['keyword']}
        여행 목적: {question['purpose']}
        여행 동반자: {question['accompany']}

        대답은
        {json}
        이렇게 일자별로 딕셔너리 형태로 대답해줘.
        """

    def ask_question(self, question):
        question_made = self.make_question(question=question)

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question_made}
            ]
        )
        content = json.loads(completion.choices[0].message.content)

        return content

