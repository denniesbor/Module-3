from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dashboard.assets import index, food
from .serializers import SearchSerializer, FoodSerializer


@api_view(['POST'])
def sentiment_view(request):
    
    # if request.method=='GET':
    #     print("get request")
    #     return Response('Ok')
    
    if request.method == 'POST':
        responses = index.returnReviews(request.data)
        serializer = SearchSerializer(data=responses)
        if serializer.is_valid():
            # print(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view()
def food_list(request):
    data = food.get_data()
    serializer = FoodSerializer(data=data)
    if serializer.is_valid():
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
