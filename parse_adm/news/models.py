# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class News(models.Model):
    title = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=32, blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'news'

    def __str__(self):
        return self.title
