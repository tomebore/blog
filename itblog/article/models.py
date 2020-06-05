from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete = models.SET_NULL, related_name = "author",null= True , blank = True)

class Article(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    author = models.ForeignKey(Author , on_delete = models.CASCADE , related_name ="articles", null= True , blank=True ) #many to one 
    readers = models.ManyToManyField(User ,related_name = "articles")
    comments = models.TextField(default = "")
    
    def __str__(self):
        return self.title 

 

