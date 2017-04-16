from django.conf.urls import url
from core.scrumboard.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^list$', RequestsListView.as_view(), name='list'),
    url(r'^create$', CreateRequestView.as_view(), name='create'),
]
