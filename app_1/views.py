from django.shortcuts import render

from .models import Article
from .serializers import Articleserializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class art_list(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = Articleserializers(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Articleserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTTP_400_BAD_REQUEST)
# Create your views here.
