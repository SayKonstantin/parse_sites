from django.urls import path
from . import views

urlpatterns = [
    path('v1/news/', views.ApiNews.as_view()),
]