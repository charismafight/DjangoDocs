from django.conf.urls import url

from .views import PublisherList, PublisherBookList, AuthorDetailView

app_name = 'myblog'
urlpatterns = [
    url(r'^publishers/$', PublisherList.as_view(), name='publishers'),
    url(r'^books/([\w-]+)/$',
        PublisherBookList.as_view(),
        name='publisherbooklist'),
    url(r'^authors/(?P<pk>[0-9]+)/$',
        AuthorDetailView.as_view(),
        name='author-detail'),
]
