from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.despesa.views import DespesaViewSet

router = routers.DefaultRouter()
router.register('despesas', DespesaViewSet, basename='despesas')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
