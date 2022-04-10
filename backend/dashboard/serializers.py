from rest_framework import serializers

class SearchSerializer(serializers.Serializer):
    content = serializers.ListField()
    search = serializers.CharField(max_length=2000)
    
class FoodSerializer(serializers.Serializer):
    available_food = serializers.ListField()


class RestaurantSerializer(serializers.Serializer):
    content = serializers.DictField()
