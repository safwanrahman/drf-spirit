from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, SerializerMethodField

from .fields import UserReadOnlyFiled
from .models import Topic, Category, Comment
from .relations import PresentableSlugRelatedField


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryLiteSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', 'slug', 'color')


class TopicSerializer(ModelSerializer):

    user = UserReadOnlyFiled()
    category = PresentableSlugRelatedField(queryset=Category.objects.all(),
                                           presentation_serializer=CategoryLiteSerializer,
                                           slug_field='slug')

    class Meta:
        model = Topic
        fields = '__all__'


class CommentSerializer(ModelSerializer):

    user = UserReadOnlyFiled()

    class Meta:
        model = Comment
        fields = '__all__'
