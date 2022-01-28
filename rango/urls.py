# Author: Zhi Kai
# Time:  15:45

from django.urls import path
from rango import views

app_name='rango'

urlpatterns = [
    path('',views.index,name='index'),
]
