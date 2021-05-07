from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    # To test the API view
    name = serializers.CharField(max_length=10)
    