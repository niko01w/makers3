from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.description}'