import os
from dotenv import load_dotenv
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TranslateTextSerializer

load_dotenv()

API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-hi"
HEADERS = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

def translate_text(text):
    result = query({"inputs": text})
    translated_text = result[0].get('translation_text', '')
    return translated_text

class TranslateTextView(APIView):
    def post(self, request):
        serializer = TranslateTextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            translated_text = translate_text(text)
            return Response({'translated_text': translated_text}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
