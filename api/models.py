from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator

# Create your models here.

#uuid or slugfy
class Meal(models.Model):

    title = models.CharField(max_length=25)
    description = models.TextField(max_length=500)

    def no_of_rating(self):
        ratings = Rating.objects.filter(meal = self)
        return len(ratings)

    def avg_rating(self):
        # sum of ratings stars / how many ratings
        sum = 0 
        ratings = Rating.objects.filter(meal = self) # nom of rating happened to the meal

        for rate in ratings:
            sum += rate.stars

        if len(ratings) > 0:
            return sum / len(ratings)
        return 0


    def __str__(self):
        return self.title


class Rating(models.Model):

    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    # Only once rating
    class Meta:
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal'),)    
