from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True, blank=True)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title