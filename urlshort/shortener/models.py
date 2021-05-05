from django.db import models

# Create your models here.


class UrlShort(models.Model):

    url = models.TextField(null=False, default='http://')
    short_url = models.CharField(max_length=25, default="xxxx")

    def __str__(self):
        return self.slug
