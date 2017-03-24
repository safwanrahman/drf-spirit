from django.conf.urls import include, url

from .views import TopicList, TopicDetails, CategoryList, CategoryDetails

app_name = 'drf-spirit'

topic_urls = [
    url(r'^$', TopicList.as_view(), name='topic-list'),
    url(r'^(?P<pk>\d+)/$', TopicDetails.as_view(), name='topic-detail')
]

category_urls = [
    url(r'^$', CategoryList.as_view(), name='category-list'),
    url(r'^(?P<slug>[-\w]+)/$', CategoryDetails.as_view(), name='category-detail')
]


urlpatterns = [
    url(r'^topics/', include(topic_urls)),
    url(r'^category/', include(category_urls)),
]
