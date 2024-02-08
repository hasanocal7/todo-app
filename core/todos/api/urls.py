from django.contrib import admin
from django.urls import path, include
from .views import ProfileListViewSet, TodoModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileListViewSet)
router.register(r'todos', TodoModelViewSet, basename='todo')


urlpatterns = [
    path('', include(router.urls)),
]
