from django.shortcuts import render, HttpResponse
from .models import   *
from django.contrib.auth.models import User
from .forms import  *

# Create your views here.
def homepage(request):
    article =Article.objects.filter(active=True)
    articles = Article.objects.all()
    wind = Author.objects.get(id=2)
    

    return render(request , "article/homepage.html", {"art": articles ,}) 

def authors(request):
    authors = Article.objects.all()
    # authors.name = request.POST.get("name")
    return render(request  , "article/author.html",
                  {"authors":authors})

def users(request):
    # context = {}
    # context["user_all"]= User.object.all()
    users_all = User.objects.all()
    return render(request  , "article/users.html",
                  {"users_all":users_all})

def detai(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, "article.html", {'article':article})

def add_article(request):
    if request.method == "POST":
        article  = Article()
        article.title = request.POST.get("title")
        article.text = request.POST.get("text")
        author_id = request.POST.get("author")
        author = Author.objects.get(id = author_id )
        article.author = author
        article.save() 

        return render(request , "article/succsess.html")
    forms =  ArticleForm()
    return render(request, "article/add_article.html", {'forms': forms})

def  profile(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, "article/profile.html", {'author': author})
    

def  add_author(request):
    if request.method == "GET":
        form = AuthorForm()
        context = {}
        context["form"] = form
        return render(request, "article/add_author.html", context)
    elif request.method == "POST":
        name = request.POST.get("name")
        user_id = request.POST.get("user")
        user = USer.objects.get(id = user_id)
        author = Author(name=name , user= user)
        author.save()
        return render(request , "article/succsess.html")  
        
   
    


