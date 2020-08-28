from django.db import models


class Person(models.Model):
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    state_of_origin = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    contact_address = models.TextField()
    id_type = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255, unique=True)


class TeamMate(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Entry(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    approved = models.BooleanField(blank=True, null=True, editable=False)
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
