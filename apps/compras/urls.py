from rest_framework import routers
from .views import ProveedorViewSet, CompraViewSet

router = routers.DefaultRouter()
router.register('api/v1/proveedores', ProveedorViewSet, 'proveedores')
router.register('api/v1/compras', CompraViewSet, 'compras')

urlpatterns = router.urls