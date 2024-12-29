from django import forms
from .models import Specialist, Service, News, Review, Achievement

class SpecialistFormModel(forms.ModelForm):
    class Meta:
        model = Specialist
        exclude = ["slug"]

class ServiceFormModel(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ["slug"]

class NewsFormModel(forms.ModelForm):
    class Meta:
        model = News
        exclude = ["slug"]

class ReviewFormModel(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["slug"]

class AchievementFormModel(forms.ModelForm):
    class Meta:
        model = Achievement
        exclude = ["slug"]