from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from article.models import Article
from article.serializers import ArticleSerializer

# Create your views here.
class ArticleViewList(APIView):

    # displat a list of all articles
    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({'articles': serializer.data}, status=status.HTTP_200_OK)

    # post a new article
    def post(self, request):
        payload = request.data
        serializer = ArticleSerializer(data=payload)
        if serializer.is_valid(raise_exception=True):
            article = serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ArticleViewDetail(APIView):

    # define a private method to get article by id
    def _article_byID(self,pk:int):
        """
        fetch an article that matches the id provided
        """
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404


    # get an article by its id
    def get(self, request, pk): 
        article = self._article_byID(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    # update an article by id
    def put(self, request, pk):
        article = self._article_byID(pk=pk)
        # create a serializer
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return JsonResponse(serializer.data)

    # delete an article by id
    def delete(self, request, pk):
        pass


           
