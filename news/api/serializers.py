from rest_framework import serializers

from home.models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['title', 'source', 'tags', 'dat_new', 'content']