from rest_framework import generics

from .models import Topic, Category
from .serializers import TopicSerializer, CategorySerializer


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
