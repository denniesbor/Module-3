from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dashboard.tests import Search
from .serializers import SearchSerializer


@api_view(['POST'])
def sentiment_view(request):
    
    # if request.method=='GET':
    #     print("get request")
    #     return Response('Ok')
    
    if request.method == 'POST':
        serializer = SearchSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view()
def collection_detail(request,pk):
    
    return Response('OK')