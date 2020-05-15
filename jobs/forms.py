from django import forms
from tinymce import TinyMCE
from .models import posts , Comment
from django.forms import ModelForm



class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return false


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols' : 30,  'rows' : 10}
        )
    )


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
