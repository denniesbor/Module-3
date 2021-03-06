from django.db import models

# Create your models here.

class TrainDfLabels(models.Model):
    business_id = models.CharField(max_length=50)
    city = models.CharField(max_length=50, default="LA")
    name = models.CharField(max_length=100, default="Taco Bell")
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
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
    Prop_pos_neg_words = models.IntegerField(default =0.0)
    sentiment_score = models.FloatField()
    sentiment = models.IntegerField(default=4)
    choice = models.TextField(default=None)
    categories = models.TextField(default = 0.0)
    
class Meals(models.Model):
    Food_Category = models.CharField(max_length=50)

class Recipe(models.Model):
    cuisine = models.CharField(max_length=50)
    diet = models.CharField(max_length=50)
    
class BusinessRestaurants(models.Model):
    business_id=models.CharField(max_length=250, primary_key=True)
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    latitude=models.FloatField()
    longitude=models.FloatField()
    stars=models.FloatField()
    stars_avg=models.FloatField()
    sentiment=models.FloatField()
    categories=models.TextField()
    categories_mod=models.TextField()
    
class Reviews(models.Model):
    business=models.ForeignKey(BusinessRestaurants, on_delete=models.PROTECT)
    review_id=models.CharField(max_length=250)
    user_id=models.CharField(max_length=250)
    review_stars=models.IntegerField()
    text = models.TextField()
    review_sentiment = models.IntegerField(default=1)
    date=models.DateField()
    

class FoodItems(models.Model):
    food_name = models.CharField(max_length=250);