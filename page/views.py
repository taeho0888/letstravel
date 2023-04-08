from django.shortcuts import render
from django.views.decorators.http import require_POST
from .chatgpt import ChatBot
import json


def InputView(request):
    return render(request, 'input.html')


@require_POST
def submit(request):
    question = {}
    for key, value in request.POST.items():
        if key != 'csrfmiddlewaretoken':
            question[key] = value  

    gpt = ChatBot()
    result = gpt.ask_question(question=question)
    # context = {'result': '{\n    "일차": {\n        "09:00": {\n            "장소": "경주 첨성대",\n            "활동": "아날로그 카메라로 첨성대와 경주시내 사진 촬영",\n            "예상경비": "무료"\n        },\n        "11:00": {\n            "장소": "안압지",\n            "활동": "아날로그 카메라로 안압지와 자연 경관 촬영",\n            "예상경비": "무료"\n        },\n        "12:30": {\n            "장소": "소풍감귤농원",\n            "활동": "필름 카메라로 소풍감귤농원에서 휴식과 촬영",\n            "예상경비": "비용당 5,000원정도"\n        },\n        "16:00": {\n            "장소": "거제도",\n            "활동": "바다와 자연 경관 감상",\n            "예상경비": "인당 25만원"\n        },\n        "20:00": {\n            "장소": "거제도 숙박시설",\n            "활동": "휴식",\n            "예상경비": "인당 20만원"\n        }\n    }\n}'}


    # result = json.loads(context['result'])

    context = { 'result' : result }
    # print(context)
    # 입력 정보 확인을 위해 입력 페이지로 이동
    return render(request, 'result.html', context)
