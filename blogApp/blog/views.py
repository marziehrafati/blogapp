from django.shortcuts import render


# Create your views here.
   # blog/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import User, Blog, UserLikeBlog
from .serializers import UserSerializer, BlogSerializer, UserLikeBlogSerializer
class RegisterView(generics.CreateAPIView):
       queryset = User.objects.all()
       serializer_class = UserSerializer

@api_view(['POST'])
def login_view(request):
       username = request.data.get('username')
       password = request.data.get('password')
       user = authenticate(username=username, password=password)
       if user is not None:
           token, created = Token.objects.get_or_create(user=user)
           return Response({'token': token.key})
       return Response({'error': 'Invalid Credentials'}, status=400)

class BlogCreateView(generics.CreateAPIView):
       queryset = Blog.objects.all()
       serializer_class = BlogSerializer
       permission_classes = [permissions.IsAuthenticated]
       def perform_create(self, serializer):
           serializer.save(author=self.request.user)

class BlogListView(generics.ListAPIView):
       queryset = Blog.objects.all()
       serializer_class = BlogSerializer

class LikeBlogView(generics.CreateAPIView):
       queryset = UserLikeBlog.objects.all()
       serializer_class = UserLikeBlogSerializer
       permission_classes = [permissions.IsAuthenticated]

       def perform_create(self, serializer):
           serializer.save(user=self.request.user)
   


