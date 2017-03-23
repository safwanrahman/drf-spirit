from django.conf.urls import include, url

import topic.urls


api = [
    url(r'^topics/', include(topic.urls, namespace='topic')),
]


urlpatterns = [
    url(r'^', include(api, namespace='drf-spirit', app_name='drf-spirit')),
]
