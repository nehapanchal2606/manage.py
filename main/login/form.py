from django import forms
from .models import user, blog


class userForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'contact']


class blogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title', 'blog', 'img']

