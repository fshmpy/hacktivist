from django.urls import path

from . import views

urlpatterns = [
    path('', views.org_homepage, name='org_homepage'),
]
