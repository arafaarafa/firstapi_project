from django.urls import path
from .views import art_list

urlpatterns = [
    path('artList/', art_list.as_view()),
]
