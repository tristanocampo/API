from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import CreateEmployeeSerializer
from .models import User

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
