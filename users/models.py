from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # the on_delete field basically says that if the User is deleted, delete the profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    # when we are trying to access any objects in this model, we get the username
    def __str__(self) -> str:
        return self.user.username
