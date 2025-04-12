from rest_framework import serializers
from .models import User

class CreateEmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        validated_data['role'] = 'EMPLOYEE'
        validated_data['is_staff'] = True  # Optional: allows admin dashboard access
        return User.objects.create_user(**validated_data)
