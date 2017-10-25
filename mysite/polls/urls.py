from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url('^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url('^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]
