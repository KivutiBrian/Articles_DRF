from rest_framework import serializers

from article.models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    author_id = serializers.IntegerField()


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