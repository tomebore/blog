from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="author_photo", null=True , blank=True)
    user = models.OneToOneField(User, on_delete = models.SET_NULL, related_name = "author",null= True , blank = True)
    



class Article(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    author = models.ForeignKey(Author , on_delete = models.CASCADE , related_name ="articles", null= True , blank=True ) #many to one 
    readers = models.ManyToManyField(User ,related_name = "articles", null=True , blank=True)
    # comments = models.TextField(default = "")
 
    
    def __str__(self):
        return self.title 

 
class Comment(models.Model):
    text = models.TextField()
    article = models.ForeignKey(Author, on_delete=models.SET_NULL , related_name = "author",null =True , blank=True)  
    user = models.ForeignKey(User , on_delete = models.CASCADE , related_name = "comment", default = "")

    def __str__(self):
        return str(self.user) + " - " + self.text  #self.user.username


