from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import firstappViewSet

firstapp_router = DefaultRouter()
firstapp_router.register(r'title', firstappViewSet)