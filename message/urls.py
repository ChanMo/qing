from django.conf.urls import url, patterns
from message import views

urlpatterns = patterns(
    "",
    url(r'^$', views.index, name='message-index'),
)
