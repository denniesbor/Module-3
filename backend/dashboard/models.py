from django.db import models

# Create your models here.

class TrainDfLabels(models.Model):
    business_id = models.CharField(max_length=50)
    review_id = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    stars = models.IntegerField()
    date = models.DateField()
    text = models.TextField()
    useful = models.IntegerField()
    funny = models.IntegerField()
    cool = models.IntegerField()
    stars_avg = models.FloatField()
    useful_avg = models.FloatField() 
    funny_avg = models.FloatField() 
    cool_avg = models.FloatField() 
    polarity = models.FloatField() 
    subjectivity = models.FloatField()
    Pos_Word_Count = models.IntegerField() 
    Neg_Word_Count = models.IntegerField() 
    sentiment = models.CharField(max_length=50) 
    sentiment_score = models.FloatField()
    
class Meals(models.Model):
    Food_Category = models.CharField(max_length=50)

class Recipe(models.Model):
    cuisine = models.CharField(max_length=50)
    diet = models.CharField(max_length=50)