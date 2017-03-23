from django.conf.urls import include, url

from .views import TopicList

app_name = 'drf-spirit'

topic_urls = [
    url(r'^', TopicList.as_view(), name='topic-list'),
]


urlpatterns = [
    url(r'^topics/', include(topic_urls)),
]
