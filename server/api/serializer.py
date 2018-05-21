from rest_framework import serializers
from .models import Message
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 
from django.views.decorators.csrf import csrf_exempt

UserModel = get_user_model()
class MessageSerializer(serializers.ModelSerializer):

    sender = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = Message
        fields = ('id', 'messageBody', 'sender' ,'date','date_modified')
        read_only_fields = ('date','date_modified')

class SignUpSerilaizer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password' ,)

class UserSerializer(serializers.ModelSerializer):

    messages = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Message.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'bucketlists')