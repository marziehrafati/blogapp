from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
   # blog/models.py

  

class User(AbstractUser):
       pass

class Blog(models.Model):
       title = models.CharField(max_length=100)
       content = models.TextField()
       author = models.ForeignKey(User, on_delete=models.CASCADE)

       def __str__(self):
           return self.title

class UserLikeBlog(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
       created_at = models.DateTimeField(auto_now_add=True)
   
