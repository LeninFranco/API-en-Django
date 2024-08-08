from rest_framework import routers
from .views import CategoriaViewSet, ProductoViewSet, InventarioViewSet

router = routers.DefaultRouter()
router.register('api/v1/categorias', CategoriaViewSet, 'categorias')
router.register('api/v1/productos', ProductoViewSet, 'productos')
router.register('api/v1/inventarios', InventarioViewSet, 'inventarios')

urlpatterns = router.urls