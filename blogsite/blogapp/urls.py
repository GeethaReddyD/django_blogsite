from django.urls import path
from .views import HomeView,ReadView,AddPostView,UpdatePostView,DeletePostView,AddCommentView,SubscriberView,new_func
urlpatterns = [
    path('home',HomeView.as_view() , name = "home"),
    path('read/<int:pk>',ReadView.as_view() ,name = 'read_detail'),
    path('addpost',AddPostView.as_view(),name = "add_post"),
    path('edit/<int:pk>',UpdatePostView.as_view(),name = 'update_post'),
    path('delete/<int:pk>',DeletePostView.as_view(),name= 'delete_post'),
    path('addcomment/<int:pk>',AddCommentView.as_view(),name = 'add_comment'),
    path('subscriber',SubscriberView.as_view() ,name ='subscribers'),
    path('demo', new_func ,name = "demo")
    
    
]
