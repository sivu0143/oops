from django.urls import path
from laptops.views import *
app_name='bobby'
urlpatterns=[
    path('hp/',hp,name='hp'),
]