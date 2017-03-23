from django.conf.urls import include, url

from .views import TopicList, TopicDetails

app_name = 'drf-spirit'

topic_urls = [
    url(r'^$', TopicList.as_view(), name='topic-list'),
    url(r'^(?P<pk>\d+)/$', TopicDetails.as_view(), name='topic-detail')
]


urlpatterns = [
    url(r'^topics/$', include(topic_urls)),
]
