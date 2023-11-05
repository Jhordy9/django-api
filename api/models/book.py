from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    class Genre(models.TextChoices):
        FICTION = "FC", _("Fiction")
        NON_FICTION = "NFC", _("Non_Fiction")
        FANTASY = "JN", _("Fantasy")
        MYSTERY = "MS", _("Mystery")
        SCIENCE_FICTION = "SFC", _("Science_Fiction")

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100, unique=True)
    genre = models.CharField(choices=Genre.choices, max_length=5)
    date = models.DateField(auto_now=False)
