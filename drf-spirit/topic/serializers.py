from rest_framework.serializers import ModelSerializer


from spirit.models import Topic


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
