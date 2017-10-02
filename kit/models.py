from __future__ import unicode_literals
from django.db import models


class KitBag(models.Model):
    kit_title = models.CharField(max_length=250)
    kit_description = models.CharField(max_length=500)
    kit_size = models.PositiveSmallIntegerField(default=1)

