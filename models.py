from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class News(models.Model):
    author = models.ForeignKey(profile,null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    news_image = models.ImageField(null=True,blank=True,default="")
    bio = models.CharField(max_length=200,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    tags = models.ManyToManyField("Tag",null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    body = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
