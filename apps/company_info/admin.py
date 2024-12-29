from django.contrib import admin
from .models import Specialist, Service, News, Review, Achievement
from .forms import SpecialistFormModel, ServiceFormModel, NewsFormModel, ReviewFormModel, AchievementFormModel

class SpecialistModelAdmin(admin.ModelAdmin):
    form = SpecialistFormModel

class ServiceModelAdmin(admin.ModelAdmin):
    form = ServiceFormModel

class NewsModelAdmin(admin.ModelAdmin):
    form = NewsFormModel

class ReviewModelAdmin(admin.ModelAdmin):
    form = ReviewFormModel

class AchievementModelAdmin(admin.ModelAdmin):
    form = AchievementFormModel

admin.site.register(Specialist,SpecialistModelAdmin)
admin.site.register(Service, ServiceModelAdmin)
admin.site.register(News, NewsModelAdmin)
admin.site.register(Review, ReviewModelAdmin)
admin.site.register(Achievement, AchievementModelAdmin)