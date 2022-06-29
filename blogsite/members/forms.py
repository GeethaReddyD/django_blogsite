from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django import forms 

class RegisterForm(UserCreationForm):
    Email = forms.EmailField()
    first_name = forms.CharField(max_length= 80)
    last_name = forms.CharField(max_length= 80)
    
    class Meta:
        model = User 
        fields = ('username','first_name','last_name','Email','password1','password2')
        widgets = {
            'username' : forms.TextInput(attrs = {'class':'form-control'}),
            'first_name' : forms.TextInput (attrs = {'class':'form-control'}),
            'last_name' : forms.TextInput(attrs = {'class': 'form-control'}),
            'Email'     : forms.TextInput(attrs = {'class': 'form-control'}),
            'password1' : forms.TextInput(attrs = {'class': 'form-control'}),
            'password2' : forms.TextInput(attrs = {'class': 'form-control'}),

        }