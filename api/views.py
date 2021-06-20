from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.serializers import Serializer
from .models import Meal ,Rating
from .serializers import MealSerializer,RatingSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
# Create your views here.
class MealViewSet(viewsets.ModelViewSet):

    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    #Decrator from viewset allow to make extra action for viw | detail = true to change value 
    @action(methods = ['post'], detail = True)
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            '''
            create or update
            '''
            meal = Meal.objects.get(id=pk)
            stars = request.data['stars'] 
            username = request.data['username']
            user = User.objects.get(username=username)

            try:
                #update
                rating = Rating.objects.get(user=user.id, meal=meal.id) #specific rate
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False) 

                json = {
                    'message':'Meal rate updated',
                    'result' : serializer.data
                }    
                return Response(json, status=status.HTTP_201_CREATED)

            except:
                #create
                rating = Rating.objects.create(user=user,stars=stars,meal=meal)    
                serializer = RatingSerializer(rating, many=False) 
                json = {
                        'message':'Meal rate crated',
                        'result' : serializer.data
                }    
                return Response(json, status=status.HTTP_200_OK)

        else:
            json = {'message':'Stars not provided'}    
            return Response(json, status=status.HTTP_200_OK)


class RatingViewSet(viewsets.ModelViewSet):

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer    

