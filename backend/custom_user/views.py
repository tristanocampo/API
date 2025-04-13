from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import CreateEmployeeSerializer
from .models import User
from django.contrib.auth import authenticate


class TestAuthenticatedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.user.role != 'ADMIN':
            return Response({'error': 'Only admin can create employees.'}, status=403)
        
        return Response({'message': 'Employee, authenticated!'}, status=status.HTTP_200_OK)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'username': user.username,
                    'role': user.role
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class CreateEmployeeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if request.user.role != 'ADMIN':
            return Response({'error': 'Only admin can create employees.'}, status=403)

        serializer = CreateEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Employee created successfully.'}, status=201)
        return Response(serializer.errors, status=400)
    
