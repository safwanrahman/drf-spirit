from django.conf.urls import url, include

from .views import TopicList


urlpatterns = [
    url(r'^', TopicList.as_view(), name='list')
]
