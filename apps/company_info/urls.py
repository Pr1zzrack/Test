from rest_framework.routers import DefaultRouter
from .views import SpecialistViewSet, ServiceViewSet, NewsViewSet, ReviewViewSet, AchievementViewSet

router = DefaultRouter()
router.register(r'specialists', SpecialistViewSet, basename='specialists')
router.register(r'serivices', ServiceViewSet, basename='services')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'achievements', ServiceViewSet, basename='achievements')
urlpatterns = router.urls