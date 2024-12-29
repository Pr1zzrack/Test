from rest_framework.routers import DefaultRouter
from .views import SignUpEyeTestViewSet


router = DefaultRouter()
router.register(r'signup-test-eye', SignUpEyeTestViewSet, basename='signup-test-eye')
urlpatterns = router.urls
