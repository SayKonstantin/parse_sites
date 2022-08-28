from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import NewsSerializer
from home.models import News
from .filters import Filter


class ApiNews(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = Filter
