from django.conf.urls import include, url
from .views import botTestingView

urlpatterns = [
	url(r'^botTesting/?$', botTestingView.as_view())
]
