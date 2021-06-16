from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from article.models import Article, Author
from article.serializers import ArticlePostSerializer, ArticlePutSerializer, ArticleSerializer, AuthorSerializer, AuthorSerializerExcludeArticles


class AuthorViewList(APIView):

    @swagger_auto_schema(
        # query_serializer=AuthorSerializerExcludeArticles,
        # operation_description="Get a list of authors",
        operation_summary="Get a list of authors",
        responses={200: AuthorSerializer(many=True)},
        # tags=['Users'],
    )
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        # operation_description="create an author",
        operation_summary="create a new author",
        request_body=AuthorSerializer,
        responses={
            200: AuthorSerializer(many=True)
        }
    )
    def post(self, request):
        payload = request.data
        serializer = AuthorSerializer(data=payload)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Create your views here.
class ArticleViewList(APIView):

    @swagger_auto_schema(
        operation_summary="get a list of articles",
        responses={
            200: ArticleSerializer(many=True)
        }
    )
    def get(self,request):
        """
        get a list of all articles
        """
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="create a new article",
        request_body=ArticlePostSerializer,
        responses={
            200: AuthorSerializer
        }
    )
    def post(self, request):
        payload = request.data
        serializer = ArticleSerializer(data=payload)
        if serializer.is_valid(raise_exception=True):
            article = serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ArticleViewDetail(APIView):

    # define a private method to get article by id
    def _article_byID(self,pk:int):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404


    @swagger_auto_schema(
        operation_summary="get an article by id",
        responses={
            200: ArticleSerializer
        }
    )
    def get(self, request, pk): 
        article = self._article_byID(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    @swagger_auto_schema(
        operation_summary="update an article",
        request_body=ArticlePutSerializer,
        responses={
            200: ArticleSerializer
        }
    )
    def put(self, request, pk):
        article = self._article_byID(pk=pk)
        # create a serializer
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    @swagger_auto_schema(
        operation_summary="delete an article",
    )
    def delete(self, request, pk):
        article = self._article_byID(pk=pk)
        article.delete()
        return Response({"message":"Record delete successfully"}, status=status.HTTP_200_OK)


           
