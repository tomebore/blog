from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="author_photo", null=True , blank=True)
    user = models.OneToOneField(User, on_delete = models.SET_NULL, related_name = "author",null= True , blank = True)

    def __str__(self):
        return self.name  
    
    class Meta:
        verbose_name = "автор" 
        verbose_name_plural = "авторы"
    



class Article(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    author = models.ForeignKey(Author , on_delete = models.CASCADE , related_name ="articles", null= True , blank=True ) #many to one 
    readers = models.ManyToManyField(User ,related_name = "articles", null=True , blank=True)
    # comments = models.TextField(default = "")

    publication_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("Tag" ,related_name="article" ,blank=True)
    picture = models.ImageField(null=True , 
        blank=True , 
        upload_to="articles/" + str(datetime.today().strftime("%Y%m%d"))
        )
    dislikes =  models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    reposts = models.IntegerField(default=0)
 
    
    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "статья" 
        verbose_name_plural = "статьи"      

 
class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Article, on_delete=models.SET_NULL , related_name = "article",null =True , blank=True)  
    author = models.ForeignKey(Author, on_delete=models.CASCADE , related_name = "author",null =True , blank=True)  
    user = models.ForeignKey(User , on_delete = models.CASCADE , related_name = "comment", default = "")

    def __str__(self):
        return str(self.user) + " - " + self.text  #self.user.username

    class Meta:
        verbose_name = "комметарий " 
        verbose_name_plural = "комментарии"
        ordering = ["user"]

class Tag (models.Model):
    name = models.CharField(max_length=55)

    class Meta:
        verbose_name = "тег" 
        verbose_name_plural = "теги"
    

