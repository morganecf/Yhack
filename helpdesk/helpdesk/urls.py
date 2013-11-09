from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

<<<<<<< HEAD
from helpdesk.views.views import helloworld
=======
#from helpdesk.views.views import helloworld
>>>>>>> 084e6ed098a387c96d1b77e4616f8b55a6d14ce1
from helpdesk.views.sessions import signup

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helpdesk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^home/', helloworld),
=======
    #url(r'^home/', helloworld),
>>>>>>> 084e6ed098a387c96d1b77e4616f8b55a6d14ce1
    url(r'^hello/', signup),
)
