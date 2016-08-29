from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sites$', views.index, name='sites'),
    url(r'^summary$', views.summary, name='summary'),
    url(r'^summary-average$', views.summary_average, name='summary_average'),
    url(r'^site/(?P<site_id>[0-9]+)/', views.site_entry, name='site_entry'),
]
