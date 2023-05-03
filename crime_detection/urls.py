from django.urls import path
from . import views
# import requests.packages.urllib3.contrib.appengine as contrib_appengine
# from OpenSSL import rand

urlpatterns = [
    path('', views.index, name='index'),
    path('result', views.result, name='result'),
    path('register_complaint', views.register_complaint, name='register_complaint'),
    path('myadmin', views.myadmin, name='myadmin')
]
