from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^home/golfer$', views.golfer_list, name='golfer_list'),

]
