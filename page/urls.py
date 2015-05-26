# page url
from django.conf.urls import url, patterns
from page.views import SiteView, IndexView, PageView
#from django.views.generic.base import RedirectView

urlpatterns = patterns(
    "",
    #url(r'^m', RedirectView.as_view(url='/', permanent=False), name='home'),
    url(r'^(?P<site_id>[0-9]+)/$', SiteView.as_view(), name='site-index'),
    url(r'^page/(?P<pk>[0-9]+)/$', PageView.as_view(), name='page-detail'),
)
