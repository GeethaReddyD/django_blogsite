from django import forms 
from .models import Post,Comment,Subscriber


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body') 

        widgets = {
            'title' : forms.TextInput(attrs = {'class':'form-control'}),
            'body' : forms.Textarea (attrs = {'class':'form-control'})
        }
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body') 

        widgets = {
            'title' : forms.TextInput(attrs = {'class':'form-control'}),
            'body' : forms.Textarea (attrs = {'class':'form-control'})
        }

class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ('name','body') 

        widgets = {
            'name' : forms.TextInput(attrs = {'class':'form-control'}),
            'body' : forms.Textarea (attrs = {'class':'form-control'})
        } 
class SubscribeForm(forms.ModelForm): 
    class Meta:
        model = Subscriber
        fields = ('name','email') 

        widgets = {
            'name' : forms.TextInput(attrs = {'class':'form-control'}),
            'email' : forms.TextInput(attrs = {'class':'form-control'})
        }
