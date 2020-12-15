from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tag(models.Model):

    title = models.CharField(max_length=256, null=False, blank=False)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Snippet(models.Model):
    tag = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title
