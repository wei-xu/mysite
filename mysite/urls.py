from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from mysite.views import hello, current_datetime

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^intern/', include('intern.urls', namespace="intern")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'^time/$', current_datetime)
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
