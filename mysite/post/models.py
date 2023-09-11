from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=255)
    date_of_create = models.DateField
    who_post = models.CharField(max_length=50)

