from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^official_jmt$', views.dining_list, name='dining_list'),
    url(r'^official_jmt_m$', views.dining_list, name='dining_list'),
    url(r'^official_jmt_w$', views.dining_list, name='dining_list'),
    url(r'^official_report$', views.official_report, name='official_report'),
    url(r'^secret_dinings$', views.secret_dinings, name='secret_dinings'),
    url(r'^mayor_best$', views.mayor_best, name='mayor_best'),
    url(r'^officials_best$', views.officials_best, name='officials_best'),
    url(r'^group_best$', views.group_best, name='group_best'),
    url(r'^price_best$', views.price_best, name='price_best'),
    url(r'^admin_best$', views.admin_best, name='admin_best'),
    url(r'^spokeman_best$', views.spokeman_best, name='spokeman_best'),

]
