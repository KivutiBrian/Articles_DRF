from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from article.models import Article
from article.serializers import ArticleSerializer

# Create your views here.
class ArticleView(APIView):

    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({'articles': serializer.data}, status=status.HTTP_200_OK)
