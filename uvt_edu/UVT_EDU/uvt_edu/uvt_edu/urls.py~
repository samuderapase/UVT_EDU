from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

      url(r'^$', 'uvt.views.index'),
    # url(r'^uvt_edu/', include('uvt_edu.foo.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
      url(r'^admin/', include(admin.site.urls)),
)
