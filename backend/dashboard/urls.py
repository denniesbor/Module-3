from django.urls import path

from .views import sentiment_view, food_list,single_restaurant_view


urlpatterns = [
    path('sentiment',sentiment_view, name = 'sentiment'),
    path('food',food_list,name='available_food'),
    path('restaurant/<slug:id>/',single_restaurant_view,name='single_restaurant')
    ]