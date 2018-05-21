# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.
class Message(models.Model):
    messageBody = models.TextField() 
    sender = models.ForeignKey('auth.User', related_name='messages', on_delete=models.CASCADE) 
    #messageSender = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.messageBody

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)