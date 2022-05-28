from .models import Comment
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class UpdateUserForm(forms.ModelForm):

    username = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email']
