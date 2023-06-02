from django.urls import path

from garage import views

urlpatterns = [
    path('contratos', views.index, name='contratos'),
    ]