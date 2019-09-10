from django.db import models
from django.contrib.auth.models import User  # import user model

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	

	def __str__(self):           #its like tostring method in java
		return f'{self.user.username} Profile'

	#objects = models.Manager()