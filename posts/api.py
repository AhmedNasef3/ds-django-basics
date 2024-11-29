from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializer

class PostListCreateAPI(ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class PostRetUpdDestAPI(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

