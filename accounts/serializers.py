from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    confirm = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm', 'email', 'first_name', 'last_name']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm']:
            raise serializers.ValidationError('password and confirm are nor the same value.')
        
        return super().validate(attrs)
