from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^process/$', views.payment_process, name='process'),
	url(r'^done/$', views.payment_done, name='done'),
	url(r'^canceled/$', views.payment_canceled, name='canceled'),
	url(r'^email_notif/$', views.email_notif, name='email_notif'),
]
