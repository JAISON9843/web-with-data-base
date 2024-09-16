from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from account.views import signup

urlpatterns=[
    re_path(r'^signup/$',signup, name="signup"),
    re_path(r'^login/$',auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    re_path(r'^logout/$',auth_views.LogoutView.as_view(next_page='home'), name="logout"),

]