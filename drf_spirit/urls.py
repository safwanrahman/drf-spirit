from django.conf.urls import include, url

from .views import TopicList, TopicDetails, TopicDetailsComments, CategoryList, CommentList

app_name = 'drf-spirit'

topic_urls = [
    url(r'^$', TopicList.as_view(), name='topic-list'),
    url(r'^(?P<slug>[\w-]+)/$', TopicDetails.as_view(), name='topic-detail'),
    url(r'^(?P<slug>[\w-]+)/comments/$', TopicDetailsComments.as_view(), name='topic-detail')
]

comment_urls = [
    url(r'^$', CommentList.as_view(), name='topic-comments'),
]

category_urls = [
    url(r'^$', CategoryList.as_view(), name='category-list'),
]


urlpatterns = [
    url(r'^topics/', include(topic_urls)),
    url(r'^categories/', include(category_urls)),
    url(r'^comments/', include(comment_urls),)
]
