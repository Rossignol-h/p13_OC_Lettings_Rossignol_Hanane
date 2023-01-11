from django.contrib.auth.models import User
from django.db import models


class ProfileImage(models.Model):
    image = models.ImageField(
        default="default-profile/default.webp", null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)
    image = models.OneToOneField(ProfileImage, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
