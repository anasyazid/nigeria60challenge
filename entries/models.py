from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    state_of_origin = models.CharField(max_length=255)
    contact_address = models.TextField()
    id_type = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255, unique=True)


class Entry(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    approved = models.BooleanField(blank=True, null=True, editable=False)
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
