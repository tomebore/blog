from django import forms
from .models import *

class ArticleForm(forms.ModelForm):
    tags = forms.CharField(max_length=255 , required=False)
    class Meta:
        model = Article 
        fields = ['title' , 'text', 'picture' ,'tags']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name' , 'user' , 'photo']


class CommentForm(forms.ModelForm):
    class Meta:
        model =  Comment
        fields = ['text' ]
   
