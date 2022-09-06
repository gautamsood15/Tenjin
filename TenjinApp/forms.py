from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, EmailInput


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={
                'required': True, 
                'placeholder': 'email', 
                'style': 'width: 350px; height: 40px; outline: none; padding: 7px;' }), 
            
            'username': forms.TextInput(attrs={
                'required': True,
                'placeholder': 'username',
                'style': 'width: 350px; height: 40px; outline: none; padding: 7px;'}),
        }


    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs = {'required': True, 'placeholder': 'password', 'style': 'width: 350px; height: 40px; outline: none; padding: 7px;'}
        self.fields['password2'].widget.attrs = {'required': True, 'placeholder': 'confirm password', 'style': 'width: 350px; height: 40px; outline: lightblue; padding: 7px;'}



class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = '__all__'

        """ widgets = {
            'username': forms.TextInput(attrs={
                'required': True, 
                'placeholder': 'Username', 
                'style': 'width: 350px; height: 40px; outline: none; padding: 7px;' }), 
            
            'password': forms.TextInput(attrs={
                'required': True,
                'placeholder': 'Password',
                'style': 'width: 350px; height: 40px; outline: none; padding: 7px;'}),
        } """
        

    username = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'placeholder': 'username', 'style': 'width: 350px; height: 40px; outline: none; padding: 7px;'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True, 'placeholder': 'password', 'style': 'width: 350px; height: 40px; outline: none; padding: 7px;'}))






