from django_filters.rest_framework import CharFilter, FilterSet

from .models import Comment


class CommentFilter(FilterSet):
    """
    A filter class for filtering comments
    """

    topic = CharFilter(name="topic__slug")
    user = CharFilter(name="user__id")

    class Meta:
        model = Comment
        fields = ['topic', 'user']
