from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from auth import views

urlpatterns = [
    path('register/', views.register),
]

# urlpatterns = format_suffix_patterns(urlpatterns)