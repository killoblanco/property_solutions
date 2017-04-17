from django.conf.urls import url, include
from core.scrumboard.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^create$', CreateRequestView.as_view(), name='create'),
    url(r'^read$', ReadRequestView.as_view(), name='read'),
    url(r'^update/(?P<pk>[0-9]+)/$', UpdateRequestView.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', DeleteRequestView.as_view(), name='delete'),
    url(r'^api/', include('core.scrumboard.api.urls', namespace='api'))
]
