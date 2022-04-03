from rest_framework import serializers

class SearchSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=200)