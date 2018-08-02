from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^input_email$', views.input_email, name='input_email'),
    url(r'^dining_list$', views.dining_list, name='dining_list'),
    url(r'^dining_list_man$', views.dining_list, name='dining_list'),
    url(r'^dining_list_women$', views.dining_list, name='dining_list'),
]
