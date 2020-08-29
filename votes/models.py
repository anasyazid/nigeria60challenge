from django.db import models


class Vote(models.Model):
    facebook_id = models.CharField(max_length=255, unique=True,
                                   error_messages="A vote has already been cast with this facebook account.")
    facebook_token = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    design_id = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
