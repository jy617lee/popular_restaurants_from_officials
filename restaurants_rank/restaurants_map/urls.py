from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^official_jmt$', views.dining_list, name='dining_list'),
    url(r'^official_jmt_m$', views.dining_list, name='dining_list'),
    url(r'^official_jmt_w$', views.dining_list, name='dining_list'),
    url(r'^official_report$', views.official_report, name='official_report'),
    url(r'^secret_dinings$', views.secret_dinings, name='secret_dinings'),
]
