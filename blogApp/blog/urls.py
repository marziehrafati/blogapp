   # blog/urls.py
from django.urls import path
from .views import RegisterView, login_view, BlogCreateView, BlogListView, LikeBlogView

urlpatterns = [
       path('register/', RegisterView.as_view(), name='register'),
       path('login/', login_view, name='login'),
       path('blogs/', BlogListView.as_view(), name='blog_list'),
       path('blogs/create/', BlogCreateView.as_view(), name='blog_create'),
       path('blogs/<int:blog_id>/like/', LikeBlogView.as_view(), name='like_blog'),
   ]
   
