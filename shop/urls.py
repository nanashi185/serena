from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	
	url(r'^about/$', views.about, name='about'),
	url(r'^menu/$', views.product_list, name='product_list'),
	url(r'^menu/(?P<category_slug>[-\w]+)/$', views.product_list,
		name='product_list_by_category'),
	url(r'^menu/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail,
		name='product_detail'),
]
