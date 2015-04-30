from django.conf.urls import url, patterns

from intern import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	# intern/study_center/
	url(r'^study_center/$', views.index_detail, name='study_center'),
	# intern/study_center/1
	url(r'^study_center/(?P<blog_id>\d+)/$', views.index_detail, name='study_center'),
	# intern/study_center/blog/1
	url(r'^study_center/blog/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	# url(r'^index_detail/$', views.index_detail, name='index_detail'),
	# intern/study_center/add_blog
	url(r'^study_center/add_blog/$', views.add_blog, name='add_blog'),
	# intern/file_center
	url(r'^file_center/$', views.file_center, name='file_center'),
	url(r'^add_file/$', views.add_file, name='add_file'),

	url(r'^wiki/$', views.wiki_index, name='wiki_index'),

	# the order of the following 3 lines cannot be reversed,
	# since the pattern in the 3rd line incorporates that in the 
	# first 2 lines 
	url(r'^wiki/(?P<wiki_pagename>[\s\S]+)/edit/$', views.wiki_edit, name='wiki_edit'),
	url(r'^wiki/(?P<wiki_pagename>[\s\S]+)/view_history/$', views.wiki_view_history, name='wiki_view_history'),
	url(r'^wiki/(?P<wiki_pagename>[\s\S]+?)/', views.wiki_index, name='wiki_index'),

	# login and register
	url(r'^login/$',views.login,name = 'login'),
	url(r'^regist/$',views.regist,name = 'regist'),
	url(r'^index1/$',views.index1,name = 'index1'),
	url(r'^logout/$',views.logout,name = 'logout'),

)
