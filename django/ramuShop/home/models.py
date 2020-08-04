from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    payment = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()