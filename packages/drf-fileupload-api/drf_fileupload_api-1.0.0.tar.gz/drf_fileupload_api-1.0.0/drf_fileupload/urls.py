from django.urls import path, include
from rest_framework import routers

from .views import FileViewSet, FileCleanView


router = routers.DefaultRouter()
router.register('', FileViewSet, basename='file-upload')

urlpatterns = [
    path('clean', FileCleanView.as_view(), name='file-clean')
] + router.urls
