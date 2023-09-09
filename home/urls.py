from django import views
from django.contrib import admin
from django.urls import path, include
from home import views 

urlpatterns = [
    path("",views.index, name="home"),
    path("subscribe", views.subscribe, name="subscribe"),
    path("confirmation", views.confirmation, name="confirmation"),
    path("send_campaign_email/", views.send_campaign_email, name="send_campaign_email"),
]