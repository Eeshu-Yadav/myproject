from rest_framework import serializers

class TranslateTextSerializer(serializers.Serializer):
    text = serializers.CharField()
