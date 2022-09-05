from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.forms import TextInput, EmailInput


class RegisterUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 350px; height: 40px; outline: none; padding: 5px;'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 350px; height: 40px; outline: none; padding: 5px;'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'password', 'style': 'width: 350px; height: 40px; outline: none; padding: 5px;'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'confirm password', 'style': 'width: 350px; height: 40px; outline: lightblue; padding: 5px;'}))


""" class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'required': True, 'placeholder': 'list@example.com', 'autofocus': True }), "username": forms.EmailInput(attrs={'placeholder': 'lisamora', })
        }


    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs = {'placeholder': 'password'}
        self.fields['password2'].widget.attrs = {'placeholder': 'confirm password'}
     """
