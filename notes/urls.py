from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<subject_id>[0-9]+)/$', views.subject_detail, name='detail'),
	url(r'^(?P<subject_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^(?P<subject_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^(?P<subject_id>[0-9]+)/(?P<note_id>[0-9]+)/$',views.note_detail, name='note_detail'),
]
