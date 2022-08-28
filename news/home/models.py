from django.db import models


class News(models.Model):
    title = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=32, blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    dat_new = models.DateField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'news'

    def __str__(self):
        return f'{self.title}'
