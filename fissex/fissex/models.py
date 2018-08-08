from django.db import models


class Thing(models.Model):
    name = models.CharField()
    note = models.TextField(null=True, blank=True)
