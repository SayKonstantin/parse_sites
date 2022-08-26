from django.shortcuts import render

from .models import News


def news(request):
    context = {'news': News.objects.all()}
    return render(request, 'news/home.html', context)
