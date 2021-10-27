from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo=models.CharField(max_length=120, help_text='title of message.')
    autor=models.CharField(max_length=120, help_text='autor of message.')

    