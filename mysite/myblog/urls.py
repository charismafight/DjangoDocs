from django.conf.urls import url

from .views import PublisherList

app_name = 'myblog'
urlpatterns = [
    url(r'^$', PublisherList.as_view(), name='publishers'),
]
