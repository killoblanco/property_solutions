from django.conf.urls import url
from web.views import OnePageView

urlpatterns = [
    url(r'^$', OnePageView.as_view(), name='landing_single_view'),
]
