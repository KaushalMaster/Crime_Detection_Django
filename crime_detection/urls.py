from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result', views.result, name='result'),
    path('register_complaint', views.register_complaint, name='register_complaint')
]
