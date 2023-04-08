from django.shortcuts import render
from django.views.decorators.http import require_POST


def InputView(request):
    return render(request, 'input.html')


@require_POST
def submit(request):
    budget = request.POST.get('budget', '')
    duration = request.POST.get('duration', '')
    keyword = request.POST.get('keyword', '')
    purpose = request.POST.get('purpose', '')
    
    # 콘솔에 출력
    print(f'budget: {budget}, duration: {duration}, keyword: {keyword}, purpose: {purpose}')
    
    # 입력 정보 확인을 위해 입력 페이지로 이동
    return render(request, 'input.html')
