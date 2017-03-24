from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .filters import CommentFilter
from .models import Topic, Category, Comment
from .serializers import TopicSerializer, CategorySerializer, CommentSerializer


class TopicList(generics.ListCreateAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()


class TopicDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()    


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()  
    lookup_field = 'slug'  


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = CommentFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
