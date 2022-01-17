from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.despesa.views import DespesaViewSet
from apps.receita.views import ReceitaViewSet

router = routers.DefaultRouter()
router.register('receita', ReceitaViewSet, basename='receita')
router.register('despesa', DespesaViewSet, basename='despesa')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
