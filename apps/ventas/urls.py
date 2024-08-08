from rest_framework import routers
from .views import ClienteViewSet, VentaViewSet

router = routers.DefaultRouter()
router.register('api/v1/clientes', ClienteViewSet, 'clientes')
router.register('api/v1/ventas', VentaViewSet, 'ventas')

urlpatterns = router.urls