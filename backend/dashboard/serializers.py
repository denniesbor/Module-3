from rest_framework import serializers

class SearchSerializer(serializers.Serializer):
    content = serializers.ListField()
    
class FoodSerializer(serializers.Serializer):
    available_food = serializers.ListField()