from django.shortcuts import render, HttpResponse
from .models import Article

# Create your views here.
def homepage(request):
    articles = Article.objects.all()

    return render(request , "article/homepage.html",{"art": articles})