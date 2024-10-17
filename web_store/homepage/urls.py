from django.urls import path

from . import views

app_name = "homepage"
urlpatterns = [
    path('', views.index, name="index"),
    path('', views.index, name="about"),
    path('', views.index, name="contact"),
]
