from rest_framework import generics

from spirit.topic.models import Topic

from .serializers import TopicSerializer


class TopicList(generics.ListAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
