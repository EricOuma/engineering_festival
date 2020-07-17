from django.db.models.signals import pre_delete
from django.dispatch import receiver
from main.models import Speaker, Sponsor

import cloudinary
import logging
logger = logging.getLogger(__name__)

@receiver(pre_delete, sender=Speaker)
@receiver(pre_delete, sender=Sponsor)
def delete_order_attachment(sender, instance, **kwargs):
    """Receives a signal of a speaker/sponsor deletion
     and delete all its photo from cloudinary
    """
    cloudinary.uploader.destroy(instance.photo, resource_type="image")