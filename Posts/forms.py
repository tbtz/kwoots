from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'type', 'date_created']
        widgets = {
            'user': forms.HiddenInput()
        }
