from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.urls.conf import include
from .views import MealViewSet ,RatingViewSet

router = routers.DefaultRouter()
router.register('meals',MealViewSet ,basename = 'meals')
router.register('ratings',RatingViewSet,basename = 'ratings')

urlpatterns = [
    path('', include(router.urls)),
    
]
