from __future__ import unicode_literals

from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible  # only if you need to support Python 2
class Carrier(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    slug_name = models.CharField(max_length=500, null=True, blank=True)

    carrier_id = models.CharField(max_length=100, unique=True)
    carrier_language = models.CharField(max_length=100, null=True, blank=True)
    carrier_cs_phone = models.CharField(max_length=200, null=True, blank=True)
    carrier_url = models.CharField(max_length=200, null=True, blank=True)
    carrier_url_tracking = models.CharField(max_length=200, null=True, blank=True)
    carrier_logo = models.CharField(max_length=100, null=True, blank=True)
    pattern_regex = ArrayField(models.CharField(max_length=1000), null=True, blank=True)

    def __str__(self):
        return unicode(self.name)


@python_2_unicode_compatible  # only if you need to support Python 2
class Event(models.Model):
    carrier = models.ManyToManyField(Carrier)

    original_event_type = models.CharField(max_length=500, null=True)
    original_time = models.CharField(max_length=500, null=True)
    original_location = models.CharField(max_length=500, null=True)
    additional_params = JSONField(null=True)

    def __str__(self):
        return unicode(self.original_event_type)
