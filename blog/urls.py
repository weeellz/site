from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post_detail/(?P<key>[0-9]+)$', views.post_detail, name='post_detail')
]