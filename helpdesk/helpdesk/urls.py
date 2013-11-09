from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#from helpdesk.views.views import helloworld
from helpdesk.views.sessions import signup

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helpdesk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^home/', helloworld),
    url(r'^hello/', signup),
)
