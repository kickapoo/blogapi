from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer
from .permissions import IsPostAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsPostAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
