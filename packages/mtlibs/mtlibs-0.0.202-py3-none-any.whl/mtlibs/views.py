from django.shortcuts import render

from django.http import HttpResponse,FileResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse


import jwt
from functools import wraps

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import permissions

def index(request):
    return HttpResponse("hello_ mtlibs")