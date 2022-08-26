from django.urls import path
from . import views
from .views import news

urlpatterns = [
    path('', views.news, name='news'),
]
