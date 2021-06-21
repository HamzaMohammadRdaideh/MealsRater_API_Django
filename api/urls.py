from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.urls.conf import include
from .views import MealViewSet ,RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('meals',MealViewSet ,basename = 'meals')
router.register('ratings',RatingViewSet,basename = 'ratings')
router.register('users',UserViewSet,basename='users')

urlpatterns = [
    path('', include(router.urls)),
    
]
