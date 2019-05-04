from .serializers import PostSerailzier
from .models import Post
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics

class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerailzier

    queryset = Post.objects.all()
