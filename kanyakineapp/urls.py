from django.conf.urls import path
from kanyakineapp import views


urlpatterns = [
    path('', views.index, name='index')
]
