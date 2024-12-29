from rest_framework import serializers
from .models import SignUpEyeTest


class SignUpEyeTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpEyeTest
        fields = '__all__'
