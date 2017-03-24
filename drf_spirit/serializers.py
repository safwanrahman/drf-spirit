from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Topic, Category, Comment


class TopicSerializer(ModelSerializer):

    user = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category


class CommentSerializer(ModelSerializer):

    user = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
