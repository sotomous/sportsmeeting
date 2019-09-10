from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#ka8e fora poy  enas xrhsths kanei eggrafh na ton apo8hkeyei sth bash dedomenwn tou profile
#neo file python
#lesson 8 at end

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()