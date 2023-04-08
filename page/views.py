from django.shortcuts import render

def InputView(request):
    return render(request, 'input.html')