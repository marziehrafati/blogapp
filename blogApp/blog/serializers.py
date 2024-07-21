   # blog/serializers.py
from rest_framework import serializers
from .models import User, Blog, UserLikeBlog

class UserSerializer(serializers.ModelSerializer):
       class Meta:
           model = User
           fields = ['id', 'username', 'email', 'password']
           extra_kwargs = {'password': {'write_only': True}}

       def create(self, validated_data):
           user = User.objects.create_user(**validated_data)
           return user

class BlogSerializer(serializers.ModelSerializer):
       author = serializers.ReadOnlyField(source='author.username')
       likes_count = serializers.IntegerField(source='userlikeblog_set.count', read_only=True)

       class Meta:
           model = Blog
           fields = ['id', 'title', 'content', 'author', 'likes_count']

class UserLikeBlogSerializer(serializers.ModelSerializer):
       class Meta:
           model = UserLikeBlog
           fields = ['id', 'user', 'blog', 'created_at']
   
