from django.shortcuts import render, HttpResponse
from .models import   *
from django.contrib.auth.models import User
from .forms import  *

# Create your views here.
def homepage(request):
    article =Article.objects.filter(active=True)
    articles = Article.objects.all()
    

    #  articles = Article.objects.raw("SELECT * FROM  aricle_article WHERE active = 0 ")  #0- false 1-True 

    return render(request , "article/homepage.html", locals() ) 

def authors(request):
    authors = Author.objects.all()
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
    comment_id = request.GET.get("text")
    comment = Comment.objects.filter(pk=comment_id)

 
    return render(request, "article.html", locals())
    

def edit_article(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST , instance=article)
        if form.is_valid():
            form.save()
            return render(request , "article/succsess.html")

    forms = ArticleForm(instance=article)
    return render(request ,"article/add_article.html", {'forms':forms})

def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request , "article/succsess.html")

        # article  = Article()
        # article.title = request.POST.get("title")
        # article.text = request.POST.get("text")
        # author_id = request.POST.get("author")
        # author = Author.objects.get(id = author_id )
        # article.author = author
        # article.save() 

    #     # return render(request , "article/succsess.html")
    forms =  ArticleForm()
    return render(request, "article/add_article.html", {'forms': forms})

def  profile(request, pk):
    author = Author.objects.get(pk=pk)
   

    return render(request, "article/profile.html", locals())
    

def  add_author(request):
    if request.method =="POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request ,  "article/succsess.html")
    form =  AuthorForm()
    return render(request, "article/add_author.html", {'form': form})


def   add_comment(request):
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request ,  "article/succsess.html")
    form =  CommentForm()
    return render(request, "article/add_comment.html", {'form': form})     
   
    


