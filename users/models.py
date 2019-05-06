from django.contrib.auth.models import User
from django.db import models

class BlogUser(models.Model):

    name = models.CharField(max_length=255)

    profile_picture = models.ImageField(null=True, blank=True, upload_to='users/%Y/%m/%d/')

    def __str__(self):

        return self.name