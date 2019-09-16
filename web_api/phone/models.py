# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    p = models.ForeignKey('Specification', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'comment'


class Specification(models.Model):
    p_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    pic = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    length = models.CharField(max_length=255, blank=True, null=True)
    width = models.CharField(max_length=255, blank=True, null=True)
    thickness = models.CharField(max_length=255, blank=True, null=True)
    weight = models.CharField(max_length=255, blank=True, null=True)
    cards = models.CharField(max_length=255, blank=True, null=True)
    sim = models.CharField(max_length=255, blank=True, null=True)
    rom = models.CharField(max_length=255, blank=True, null=True)
    ram = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)
    front = models.CharField(max_length=255, blank=True, null=True)
    cameras = models.CharField(max_length=255, blank=True, null=True)
    back = models.CharField(max_length=255, blank=True, null=True)
    power = models.CharField(max_length=255, blank=True, null=True)
    earphone = models.CharField(max_length=255, blank=True, null=True)
    thunderport = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'specification'
