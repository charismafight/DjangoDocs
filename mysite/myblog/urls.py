from django.conf.urls import url

from .views import PublisherList, PublisherBookList, AuthorDetailView, CreateAuthor, UpdateAuthor, DeleteView

app_name = 'myblog'
urlpatterns = [
    url(r'^publishers/$', PublisherList.as_view(), name='publishers'),
    url(r'^books/([\w-]+)/$',
        PublisherBookList.as_view(),
        name='publisherbooklist'),
    url(r'^authors/(?P<pk>[0-9]+)/$',
        AuthorDetailView.as_view(),
        name='author-detail'),
    url(r'^author/add/$', CreateAuthor.as_view(), name='create-author'),
    url(r'^author/(?P<pk>[0-9]+)/$',
        UpdateAuthor.as_view(),
        name='update-author'),
    url(r'^author/(?P<pk>[0-9]+)/delete/$',
        DeleteView.as_view(),
        name='delete-author'),
]
