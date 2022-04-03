from django.urls import path

from .views import sentiment_view, collection_detail


urlpatterns = [
    path('sentiment',sentiment_view, name = 'sentiment'),
    path('collection/<int:pk>',collection_detail,name='collection-detail')
    ]