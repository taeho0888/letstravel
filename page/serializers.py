from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['month','duration','where','budget','keyword','purpose','accompany','answer']