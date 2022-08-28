import django_filters

from home.models import News


class Filter(django_filters.FilterSet):
    source = django_filters.CharFilter()
    tags = django_filters.CharFilter()
    dat_new = django_filters.DateFromToRangeFilter()

    class Meta:
        model = News
        fields = ['source', 'tags', 'dat_new']
