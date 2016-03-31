from __future__ import unicode_literals

from django.db import models


class Place(models.Model):
    place_name = models.CharField(max_length=50)
    geo_location = models.CharField(max_length=100)
    place_id = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    local_phone_number = models.CharField(max_length=16, blank=True, null=True)
    international_phone_number = models.CharField(
        max_length=16, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    icon = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.place_name


class Photo(models.Model):
    photo_name = models.CharField(max_length=100, blank=True, null=True)
    place = models.ForeignKey(Place)
    url = models.URLField()
    mimetype = models.CharField(max_length=100)

    def __str__(self):
        return self.photo_name


class Types(models.Model):
    type_name = models.CharField(max_length=40)

    def __str__(self):
        return self.type_name
