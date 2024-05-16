
from rest_framework.routers import DefaultRouter
from .views import PokeAPIService


router = DefaultRouter()
router.register('pokemon', PokeAPIService)

urlpatterns = router.urls

