# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics,permissions
from .serializer import MessageSerializer,UserSerializer,SignUpSerilaizer
from .models import Message
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class CreateMessage(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create_message(self, serializer):
        serializer.save()
    
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user) 


class CreateUser(generics.ListCreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = SignUpSerilaizer
         
class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer