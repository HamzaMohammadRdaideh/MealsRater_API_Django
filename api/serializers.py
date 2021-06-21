import re
from django.contrib.auth.models import User
from django.db import models 
from django.db.models import fields
from rest_framework import serializers
from .models import Meal, Rating

class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = ('id','title','description','no_of_rating','avg_rating')


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('id','stars','user','meal')        


class UserSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = User
        fields = ('username', 'password')
        # password not return in json
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    
