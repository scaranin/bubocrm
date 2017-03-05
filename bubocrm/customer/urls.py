from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	#url(r'^data_customer/', views.data_customer, name='data_customer'),
    url(r'^data_customer/(?P<customer_id>[0-9]+)/$', views.data_customer, name='data_customer'),
]