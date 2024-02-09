from django.urls import path, include
from rest_framework import routers
from cps import views

# Api versioning
router = routers.DefaultRouter()
router.register(r'finishgood', views.FinishGoodView, 'finishgood')
router.register(r'componente', views.ComponenteView, 'componente')
router.register(r'bom', views.BOMView, 'bom')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    # Añade tu nueva ruta aquí
    path("api/v1/finishgoodbom/<str:referencia>/", views.FinishGoodBOMView.as_view(), name='finishgood-bom'),
]