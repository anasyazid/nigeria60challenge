from django.db import models


class Vote(models.Model):
    facebook_id = models.CharField(max_length=255, unique=True)
    design_id = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
