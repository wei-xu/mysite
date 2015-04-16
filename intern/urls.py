from django.conf.urls import url, patterns

from intern import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^index_detail/$', views.index_detail, name='index_detail'),
	url(r'^add_blog/$', views.add_blog, name='add_blog'),
)