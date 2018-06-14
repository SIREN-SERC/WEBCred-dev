from django.db import models
from django.contrib.postgres.fields import JSONField


class Record(models.Model):
    url = models.URLField(max_length=256)
    dump = JSONField()
    modified_time = models.IntegerField()
