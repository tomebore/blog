from django.shortcuts import render, HttpResponse
from .models import Article , Author

# Create your views here.
def homepage(request):
    articles = Article.objects.all()
    wind = Author.objects.get(id=2)
    

    return render(request , "article/homepage.html",
                    {"art": articles ,
                    "wind" : wind}
                    )