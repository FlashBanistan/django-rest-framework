from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView
    )
from posts.models import Post
from .serializers import (
    PostCreateSerializer,
    PostDetailSerializer,
    PostListSerializer
    )


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
