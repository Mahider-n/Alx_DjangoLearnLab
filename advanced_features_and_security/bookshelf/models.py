from django.db import models
from django.conf import settings

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # references your custom user
        on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True)