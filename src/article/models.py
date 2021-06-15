from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(blank=False, max_length=255)
    email = models.EmailField(blank=True, null=True)

    def __str__(self) -> str:
        return self.email

# article model
class Article(models.Model):
    title = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=False)
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title