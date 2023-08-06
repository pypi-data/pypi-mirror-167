from django.urls import path
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('protected/', views.protected_page,name="protected_page"),
]
