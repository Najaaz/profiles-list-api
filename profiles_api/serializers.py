from django.contrib.admin import filters
from django.contrib.auth import models
from rest_framework import serializers
from django.contrib.auth.models import User
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    # To test the API view
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','username','first_name','email', 'password')
        extra_kwargs = {
            'password':{'write_only':True, 'style':{'input_type':'password'}},
        }

    def create (self, validated_data):
        # Create and return a new user
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            password = validated_data['password']
        )

        return user



class ProfileFeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileFeed
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile':{"read_only":True}}

