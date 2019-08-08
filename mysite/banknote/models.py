import uuid

from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserTimeStampedModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,
                                   related_name="%(app_label)s_%(class)s_created_by", related_query_name="%(app_label)s_%(class)s_created_by")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT,
                                   related_name="%(app_label)s_%(class)s_updated_by", related_query_name="%(app_label)s_%(class)s_updated_by")
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('updated_on', 'created_on')


class Person(UserTimeStampedModel):
    name = models.CharField(max_length=50, db_index=True)
    contact = PhoneNumberField('Contact number', unique=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
        # return '{}: {}'.format(self.name, self.contact)


class Appraisal(UserTimeStampedModel):
    id_num = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    country = models.CharField(max_length=50, blank=True)
    series = models.CharField(max_length=50, blank=True)
    serial_number = models.CharField(max_length=50, blank=True)
    grading = models.CharField(max_length=50, blank=True)
    inferred = models.CharField(max_length=50, blank=True)
    denomination = models.CharField(max_length=50, blank=True)
    variety = models.CharField(max_length=50, blank=True)
    customer = models.ForeignKey(Person, on_delete=models.PROTECT)
    appraiser = models.ForeignKey(User, on_delete=models.PROTECT)
    remarks = models.TextField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='uploads/', blank=True)


