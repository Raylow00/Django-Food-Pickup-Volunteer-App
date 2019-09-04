from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from multiselectfield import MultiSelectField
# Create your models here.

CHOICES = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)


'''class UserManager(BaseUserManager):
    def createUser(self, username, password, email, IC_number):
        if not email and IC_number:
            raise ValueError('Users must have an email and IC number')
        user = self.model(
            username=username,
            email = self.normalize_email(email),
            IC_number = IC_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def createSuperuser(self, username, password, email, IC_number):
        user = self.createUser(username, email, password, IC_number)
        user.is_admin = True
        user.save(using=self._db)
        return user
'''

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password1 = models.CharField(max_length=20, blank=False, null=False)
    password2 = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    address = models.TextField()
    details_days = MultiSelectField(max_length=100, max_choices=7, choices=CHOICES)
    details_time = models.TextField()
    volunteers = models.IntegerField()
    pin = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Registration(models.Model):
    user = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now, blank=True, null=True)
    key = models.ForeignKey(Event, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    tagged = ArrayField(models.CharField(max_length=50), blank=True, null=True)
