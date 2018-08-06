from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^input_email$', views.input_email, name='input_email'),
    url(r'^official_jmt$', views.dining_list, name='dining_list'),
    url(r'^official_jmt_m$', views.dining_list, name='dining_list'),
    url(r'^official_jmt_w$', views.dining_list, name='dining_list'),
]
