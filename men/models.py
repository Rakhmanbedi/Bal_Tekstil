from django.db import models

class Men(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

class Post(models.Model):
     discription = models.TextField(blank=True)
     price = models.IntegerField()
     size = models.CharField(max_length=255)
     image = models.ImageField(upload_to="photos/%Y/%m/%d/")
     time_update = models.DateTimeField(auto_now_add=True)
     is_published = models.BooleanField(default=True)

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")

class comments(models.Model):
    comment = models.TextField(blank=True)

class Categories(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

class Roles(models.Model):
    name = models.CharField(max_length=20)
