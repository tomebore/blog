from django.shortcuts import render, HttpResponse
from .models import   *
from django.contrib.auth.models import User
from .forms import  *
from django.db.models import Q

# Create your views here.
def homepage(request):
    if  "key_word" in request.GET:
        key = request.GET.get("key_word")
        article = Article.objects.filter(Q(active=True) , Q(title__contains=key) , 
                    Q(text__contains=key) | Q(tags__name__contains=key)|
                        Q(readers__username__contains=key)| Q(picture__contains=key)|
                            Q(picture__contains=key)| Q(comments__text__contains=key))
        article = article.distinct()
    else:
        article =Article.objects.filter(active=True)

    return render(request , "article/homepage.html", locals() ) 

def articles(request,tag):
    context={}
    tag = Tag.objects.get(name=tag)
    context["articles"]= Article.objects.filter(tag=tag)
    return render(request, "articles.html",context)

def authors(request):
    authors = Author.objects.all()
    return render(request  , "article/author.html",
                  {"authors":authors})

def users(request):
    users_all = User.objects.all()
    return render(request  , "article/users.html",
                  {"users_all":users_all})

def detai(request, pk):
    article = Article.objects.get(pk=pk)
    article.views +=1
    user = request.user
    if not user.is_anonymous:
        article.readers.add(user)
    article.save()


    if request.method =="POST":
        if "delete_btn" in request.POST:
            article = Article.objects.get(pk=pk)
            article.active = False
            article.save()
            return redirect(homepage)
        elif "add_comment_btn" in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = Comment()
                comment.user = request.user 
                comment.article  = article
                comment.text = form.cleaned_data["text"]
                comment.save()

    context = {}
    context["article"] = Article.objects.get(pk=pk)
    context["form"] = CommentForm()

    return render(request, "article.html", context )
    

def edit_article (request,pk):
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST ,request.FILES ,instance=article)
        if form.is_valid():
            article.title = form.cleaned_data["title"]
            article.text = form.cleaned_data["text"]
            article.picture = form.cleaned_data["picture"]
            article.save()

            tags = form.cleaned_data["tags"]
            for tag in  tags.split(","):
                obj,created = Tag.objects.get_or_create(name=tag)
                article.tag.add(obj)
            
            article.save()
            context = {}
            context["article"] = article
            context["form"] = CommentForm()
            context["message"] = "Статья была изменена успешно!"

            
            return render(request , "article/succsess.html",context)

    forms = ArticleForm(instance=article)
    return render(request ,"article/add_article.html", {'forms':forms})


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST ,request.FILES)
        if form.is_valid():
            if not  Author.objects.filter(user=request.user):
                author =  Author(
                    user= request.user ,
                    name= request.user.username 
                )
                author.save()
            else:
                author = Author.objects.get(user=request.user )

            article = Article()
            article.author = author
            article.title = form.cleaned_data["title"]
            article.text = form.cleaned_data["text"]
            article.picture = form.cleaned_data["picture"]
            article.save()
            

            tags = form.cleaned_data["tags"]
            for tag in  tags.split(","):
                obj,created = Tag.objects.get_or_create(name=tag)
                article.tag.add(obj)
            
            article.save()
            return render(request , "article/succsess.html")

    forms =  ArticleForm()
    return render(request, "article/add_article.html", {'forms': forms})

def  profile(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, "article/profile.html", locals())
    

def  add_author(request):
    if request.method =="GET":
        form = AuthorForm()
        context = {}
        context["form"] = form
        return render(request,"article/add_author.html",context)

    elif request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"article/success.html")

def edit_comment (request,pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST , instance=comment)
        if form.is_valid():
            form.save()
            return render(request , "article/succsess.html")

    forms = CommentForm(instance=comment)
    return render(request ,"article/comment_form.html", {'forms':forms})
       
def delete_comment(request,pk):
    Comment.objects.get(pk=pk).delete()
    return render(request,"article/success.html")
    


