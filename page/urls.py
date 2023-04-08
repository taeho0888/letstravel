from django.urls import path
from .views import *

urlpatterns = [
    path('input', InputView, name='InputView'),
]
