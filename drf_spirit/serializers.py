from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Topic, Category, Comment


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class TopicSerializer(ModelSerializer):

    user = PrimaryKeyRelatedField(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'


class CommentSerializer(ModelSerializer):

    user = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
