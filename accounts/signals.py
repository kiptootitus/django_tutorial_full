from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from accounts.models import Profile


@receiver([post_save, post_delete], sender=Profile)
def invalidate_profile_cache(sender, instance, **kwargs):
    """_summary_
      This will upsate the list of the profiles when it is deleted, created, update,
    Args:
        sender (_type_): _description_
        instance (_type_): _description_
    """

    print("Cleaning Profile cache")

    # TODO
    cache.delete_pattern('*profile_list*')
