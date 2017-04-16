from django.conf.urls import url, include

urlpatterns = [
    url(r'^scrumboard/', include('core.scrumboard.urls', namespace="scrumboard")),
]
