from django.urls import path
from .views import *

urlpatterns = [
    path('input', input_view, name='InputView'),
    path('submit', submit, name="submit"),
    path('result', result, name='result'),
    path('result/<int:pk>', ChatView.as_view({'get':'retrieve'}), name='user_result'),
]
