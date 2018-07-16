from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.input_email, name='input_email'),
]
