from django.conf.urls import url

from . import views # . from the same root

urlpatterns = [
	url(r'^$',views.index,name='index'),
]
#