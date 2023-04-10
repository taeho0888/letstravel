from django.shortcuts import render
from django.views.decorators.http import require_POST
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response


def input_view(request):
    return render(request, 'input.html')

@require_POST
def submit(request):
    # POST 요청으로부터 유저 모델 데이터 추출
    user_data = {
        'month': request.POST.get('month'),
        'duration': request.POST.get('duration'),
        'where': request.POST.get('where', '추천해줘'),
        'budget': request.POST.get('budget'),
        'keyword': request.POST.get('keyword'),
        'purpose': request.POST.get('purpose'),
        'accompany': request.POST.get('accompany'),
    }

    # 유저 모델 생성
    user = User.objects.create(
        month=user_data['month'],
        duration=user_data['duration'],
        where=user_data['where'],
        budget=user_data['budget'],
        keyword=user_data['keyword'],
        purpose=user_data['purpose'],
        accompany=user_data['accompany'],
    )

    return render(request, 'result.html', context={'id': user.pk})

def result(request):
    pass

class ChatView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer