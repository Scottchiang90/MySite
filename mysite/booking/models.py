from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.dateformat import format

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    contact = PhoneNumberField('Contact number', unique=True)
    email = models.EmailField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {}'.format(self.name, self.contact)

class Booking(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True, blank=True)
    book_dt = models.DateTimeField('Booking date time')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        datetime_str = format(self.book_dt, settings.SHORT_DATETIME_FORMAT)
        return '{}-{}'.format(self.person.name, datetime_str)
