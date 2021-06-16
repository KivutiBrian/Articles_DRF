from rest_framework import serializers

from article.models import Article, Author

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()

    articles = serializers.SlugRelatedField(many=True, read_only=True, slug_field="title")
    

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class AuthorSerializerExcludeArticles(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)


class ArticlePutSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()

class ArticlePostSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    author_id = serializers.IntegerField()

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    author_id = serializers.IntegerField()
    
    # author = serializers.SlugRelatedField(queryset=Author.objects.all(), many=False, slug_field="name")
    author = AuthorSerializerExcludeArticles(read_only=True)


    """
    if object instances correspond to Django models then, ensure that these methods save the objects to the datbase
    .save() will create an a new instance or update existing instances
    """
    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.description)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.save()
        return instance