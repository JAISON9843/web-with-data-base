from django.urls import path,re_path

from . import views

urlpatterns=[
    path("",views.home, name="home"),
    path("about", views.about, name="about"),
    path("dlmadd", views.dlmadd, name="dlamadd"),
    path("viewdlm", views.viewdlm, name="viewdlm"),
    re_path(r'^(?P<pk>\d+)/update/$',views.editdlm,name='editdlm'),
    re_path(r'^(?P<pk>\d+)/delete/$',views.deletedlm,name='deletedlm')

]