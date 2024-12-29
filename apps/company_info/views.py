from rest_framework.viewsets import ModelViewSet
from .models import Specialist, Service, News, Review, Achievement
from .serializers import SpecialistSerializer, ServiceSerializer, NewsSerializer, ReviewSerializer, AchievementSerializer

class SpecialistViewSet(ModelViewSet):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class AchievementViewSet(ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer