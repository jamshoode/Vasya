from rest_framework import serializers

from .models import Student

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', )