from rest_framework import serializers
from rest_framework import response
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.serializers import Serializer
from .models import Meal ,Rating
from .serializers import MealSerializer,RatingSerializer,UserSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token

# Create your views here.
class MealViewSet(viewsets.ModelViewSet):

    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    # authentication_classes = (TokenAuthentication,)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    #http://127.0.0.1:8000/api/meals/meal_pk/rate_meal
    # requsets => stars + user
    # pk from url
    #Decrator from viewset allow to make extra action for viw | detail = true to change value 
    @action(methods = ['post'], detail = True)
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            '''
            create or update
            '''
            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user 


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

    # authentication_classes = (TokenAuthentication,)
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        response = {
            'meassage':'Invalid way to Create or Update'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {
            'meassage':'Invalid way to Create or Update'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)    


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        username = request.data['username']
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({
                'token ': token.key,
                'username ': username
                }, 
            status=status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        response = {'message': 'You cant create user like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)