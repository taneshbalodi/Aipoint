from django import forms

from .models import posts , Comment
from django.forms import ModelForm







    class Meta:
        model = posts
        fields = ('title', 'overview', 'content', 'thumbnail',
        'categories', 'featured', 'previous_post', 'next_post')


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
    'class': 'form-control',
    'placeholder': 'Type your comment',
    'id': 'usercomment'

    }))

    class Meta:
        model = Comment
        fields = ('content',)
