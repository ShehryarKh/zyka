from django.conf.urls import url
from django.contrib import admin
from zyka import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='home'),

]