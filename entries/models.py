from django.db import models


class Person(models.Model):
    team_members = models.CharField(max_length=255, blank=True, null=True)
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
    slogan = models.CharField(max_length=255, blank=True, null=True)
    poem = models.CharField(max_length=255, blank=True, null=True)
    poem_url = models.CharField(max_length=255, blank=True, null=True)
    pic_1 = models.ImageField(upload_to='uploads', blank=True, null=True)
    pic_2 = models.ImageField(upload_to='uploads', blank=True, null=True)
    pic_3 = models.ImageField(upload_to='uploads', blank=True, null=True)
    approved = models.BooleanField(blank=True, null=True, editable=False)
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
