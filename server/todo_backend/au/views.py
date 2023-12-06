from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json
# Create your views here.
@api_view(['POST'])
def verify(request):
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    if(authenticate(username=body_data['name'],password=body_data['pass']) is not None):
        res=Response(status=status.HTTP_202_ACCEPTED)
        res.set_cookie(
                    key="name",  # Cookie name
        value=body_data['name'],  # Cookie value
        max_age=6000,  # Max age of the cookie in seconds (e.g., 1 hour)
        secure=False,  # Set to True for HTTPS only
        httponly=False,  # Cookie can't be accessed via JavaScript
        samesite="None",  # Set the SameSite attribute (Lax, Strict, None)
        domain="http://localhost:8080",  # Optional: specify the domain for the cookie
        path="/",  # Optional: specify the path for the cookie
        )
        return  res  
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def register(request):
   body_unicode = request.body.decode('utf-8')
   body_data = json.loads(body_unicode)
   try:
       User.objects.create_user(username=body_data['name'],password=body_data['pass'])
   except Exception as e:
       print(e)    
       return Response(data={'error'},status=status.HTTP_400_BAD_REQUEST)
   return Response(status=status.HTTP_201_CREATED)
