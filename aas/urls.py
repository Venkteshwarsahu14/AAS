from .views import VehicleViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter  # we can use custom routers

router = SimpleRouter()

router.register('' , VehicleViewSet)


urlpatterns = router.urls


