from django.db import models


class Vote(models.Model):
    facebook_id = models.CharField('Facebook account', max_length=255, unique=True)
    facebook_token = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    design_id = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
