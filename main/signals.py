# from main.models import Program
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from main import sls_calendar

# @receiver(post_save, sender=Program)
# def save_program_to_google_calendar(sender, instance, **kwargs):
#     sls_calendar.create_event(instance)