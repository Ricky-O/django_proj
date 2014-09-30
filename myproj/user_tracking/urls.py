from django.conf.urls import patterns, url
from user_tracking import views
from django.views.generic import RedirectView
from models import User, Access
from django.conf.urls import patterns
from django.views.generic import TemplateView

from django.utils.html import urlize

user1 = User.objects.get(pk=1)
url_to = user1.get_url()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index.html', TemplateView.as_view(template_name="index.html")),

    #redirects to a url in the database
    url(r'^/r/', RedirectView.as_view(url=url_to), name='redirect'),

    url(r'^/$', views.root, name='root'),

    #url(r'^(?P<user_id>\d+)/$', views.detail, name='detail'),

    #url(r'^(?P<user_id>\d+)/$', views.name, name='name'),

    #url(r'^(?P<user_id>\d+)/$', views.time, name='time'),
)

