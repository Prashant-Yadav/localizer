from __future__ import unicode_literals

from django.db import models


class Place(models.Model):
    place_name = models.CharField(max_length=50)
    geo_location = models.CharField(max_length=100)
    place_id = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    local_phone_number = models.IntegerField()
    international_phone_number = models.IntegerField()
    website = models.URLField()
    icon = models.URLField()

    def __str__(self):
        return self.place_name


class Photo(models.Model):
    photo_name = models.CharField(max_length=100)
    place = models.ForeignKey(Place)
    url = models.URLField()
    mimetype = models.CharField(max_length=100)

    def __str__(self):
        return self.photo_name


class Types(models.Model):
    type_name = models.CharField(max_length=40)

    def __str__(self):
        return self.type_name
