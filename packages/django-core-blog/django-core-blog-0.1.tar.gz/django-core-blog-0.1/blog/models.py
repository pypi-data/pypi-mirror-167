from django.db import models


# Create your models here.

class Post(models.Model):
    class Meta:
        abstract = True

    content = models.TextField()