from django.urls import path

from national import views

urlpatterns = [
    path('', views.index, name='index'),
]