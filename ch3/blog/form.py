from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post #,있으면 error 'tuple' object has no attribute '_meta'
        fields = ['title','author','content']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text']
