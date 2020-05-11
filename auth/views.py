from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from auth.serializers.user_serializer import UserSerializer
from auth.models.user import User
import uuid


# Create your views here.
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    final_data = {}
    if serializer.is_valid():
        saved_user = serializer.save()
        data = serializer.data
        token = Token.objects.get(user=saved_user).key
        status_code = status.HTTP_201_CREATED
        message = 'User created successfully.'
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        message = serializer.errors
        data = None
        token = None

    final_data['status_code'] = status_code
    final_data['message'] = message
    final_data['data'] = data
    final_data['token'] = token
    return Response(data=final_data, status=status_code, content_type="application/json")
