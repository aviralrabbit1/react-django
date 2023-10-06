from django.urls import path, include
from rest_framework.routers import DefaultRouter
from firstapp.api.urls import firstapp_router

router = DefaultRouter()

router.registry.extend(firstapp_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
