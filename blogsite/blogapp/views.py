from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse_lazy 
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comment,Subscriber 
from .forms import CommentForm,PostForm,EditForm,SubscribeForm
from django.urls import reverse_lazy,reverse
from django.core.mail  import send_mail
from .tasks import test


# Create your views here.
# To fetch all the posts from Posts table
class HomeView(ListView):
    model = Post 
    template_name = 'home.html'

# To fetch single post using primary key
class ReadView(DetailView):
    model = Post 
    template_name = 'read_detail.html'

# To add new post to table
class AddPostView(CreateView):
    
    model = Post 
    form_class = PostForm
    
    template_name = 'add_post.html' 
    success_url = reverse_lazy('demo')
    

    
    # To get the current author for the post
    def form_valid(self,form):
    
        form.instance.author = self.request.user
        
        return super().form_valid(form)
    
# To update the details of the posts        
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm 
    template_name = 'update_post.html'

# To delete the posts from the table
class DeletePostView(DeleteView):
    model = Post 
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

# To add comments to the posts
class AddCommentView(CreateView):
    
    model = Comment
    form_class = CommentForm
    template_name = 'comment.html' 

    # To get the current post id
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        
        return super().form_valid(form)


# To add the subscribers to the table
class SubscriberView(CreateView):
        model = Subscriber 
        form_class = SubscribeForm 
        template_name = "subscriber.html" 

def new_func(request):
    test.delay() 
    return redirect('home')




    



    







