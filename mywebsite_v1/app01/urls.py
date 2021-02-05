
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^index$', views.index), # 首页
    url(r'^login_check$', views.login_check), # 首页
    url(r'^userpage$', views.userpage), # 首页
    url(r'^sign_up_check',views.sign_up_check),
    url(r'^sign_up',views.sign_up),
]