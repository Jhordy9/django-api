from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150, unique=True)
