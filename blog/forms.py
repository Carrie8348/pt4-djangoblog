from .models import Comment
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ProfileForm(forms.Form):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=150)