from django.conf.urls import url
from web import views

urlpatterns = [
    url(r'^$', views.landing_single_view, name='landing_single_view'),
]
