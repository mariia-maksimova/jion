from django.db import models
from django.forms import ModelForm

# Create your models here.

class LoginForm(models.Model):
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100)
