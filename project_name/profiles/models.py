import os
import uuid

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


def avatar_upload(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("avatars", filename)


class Profile(models.Model):

    user = models.OneToOneField(User)
    name = models.CharField(max_length=75, blank=True)
    avatar = models.ImageField(upload_to=avatar_upload, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=250, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.modified_at = timezone.now()
        return super(Profile, self).save(*args, **kwargs)
