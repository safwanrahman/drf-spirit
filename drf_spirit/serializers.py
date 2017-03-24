from rest_framework.serializers import ModelSerializer


from .models import Topic, Category


class TopicSerializer(ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'slug'
