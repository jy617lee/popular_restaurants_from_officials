from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^input_email$', views.input_email, name='input_email'),
<<<<<<< HEAD
    url(r'^official_jmt$', views.dining_list, name='dining_list'),
    url(r'^official_jmt_m$', views.dining_list, name='dining_list'),
    url(r'^official_jmt_w$', views.dining_list, name='dining_list'),
=======
    url(r'^dining_list$', views.dining_list, name='dining_list'),
    url(r'^dining_list_m$', views.dining_list, name='dining_list'),
    url(r'^dining_list_w$', views.dining_list, name='dining_list'),
>>>>>>> url 수정, css 수정
]
