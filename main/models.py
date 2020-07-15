import cloudinary

from django.db import models
from django.contrib.postgres.fields import CICharField, CIEmailField
from django.core.validators import validate_email, MaxLengthValidator, MinLengthValidator
from cloudinary.models import CloudinaryField
from django.core.exceptions import SuspiciousOperation

# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
# from main import sls_calendar

# Create your models here.
class Speaker(models.Model):
    title = models.CharField(max_length=35, help_text="eg <em>Mr, Dr, Prof...</em>.", blank=True, null=True)
    full_name = models.CharField(max_length=35)
    role = models.CharField(max_length=100, help_text="eg <em>CEO Google</em>.", blank=True, null=True)
    photo = CloudinaryField('image')
    facebook_url = models.URLField(max_length=200, blank=True, null=True)
    instagram_url = models.URLField(max_length=200, blank=True, null=True)
    twitter_url = models.URLField(max_length=200, blank=True, null=True)
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        if self.title:
            return f'{self.title}.  {self.full_name}'
        else:
            return self.full_name


class SummitDay(models.Model):
    DAY_CHOICES = [
        ('1', 'ONE'),
        ('2', 'TWO'),
        ('3', 'THREE'),
    ]
    day_number = models.CharField(max_length=5, choices=DAY_CHOICES, blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f'SummitDay {self.day_number}'


class Program(models.Model):
    """The Daily sls programs"""
    day = models.ForeignKey('SummitDay', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=40)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # write a custom validator so that the end time comes after the start time
    description = models.TextField()
    venue = models.CharField(max_length=30)
    speaker = models.ForeignKey('Speaker', models.SET_NULL, blank=True, null=True)
    google_event_id = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.name



class Sponsor(models.Model):
    name = models.CharField(max_length=40)
    logo = CloudinaryField('image')



# @receiver(post_save, sender=Program)
# def save_program_to_google_calendar(sender, instance, created, **kwargs):
#     if created:
#         sls_calendar.create_event(instance)


# @receiver(post_save, sender=Program)
# def update_program_on_google_calendar(sender, instance, created, **kwargs):
#     # created = False
#     if not created:
#         print('Updating to Google')
#         sls_calendar.update_event(instance, instance.google_event_id)

# write a signal for deleting images from cloudinary