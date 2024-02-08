from todos.models import UserProfile, Todo
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Todo
        fields = '__all__'