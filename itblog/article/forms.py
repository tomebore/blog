from django import forms
from .models import *

class ArticleForm(forms.ModelForm):
    tag = forms.CharField(max_length=255 , required=False)
    class Meta:
        model = Article 
        fields = ['title' , 'text', 'picture' ,'tag']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name' , 'user' , 'photo']


class CommentForm(forms.ModelForm):
    class Meta:
        model =  Comment
        fields = ['text' ]
   
