from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import Person, Entry


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class EntrySerializer(WritableNestedModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = Entry
        fields = '__all__'
