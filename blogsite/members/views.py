from django.shortcuts import render
from django.views import generic 
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
from .forms import RegisterForm

# Create your views here.
# To register the new users

class UserRegistration(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html' 
    success_url = reverse_lazy('login') 

    # We can fetch the current user who has registered
    def form_valid(self,form):
        form.instance.user = self.request.user 
        return super().form_valid(form)



