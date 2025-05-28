from django.db import models

# Create your models here.
class Subscribe(models.Model):
    email = models.EmailField()


class Partner(models.Model):
    logo = models.ImageField(upload_to='partners/')


class Contact(models.Model):
    instagram = models.URLField()
    telegram = models.URLField()
    youtube = models.URLField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)


class ContactUs(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
