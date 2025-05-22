from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('company', 'Company'),
        ('freelancer', 'Freelancer'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

class Project(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects', limit_choices_to={'user_type': 'company'})
    title = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    skills = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Portfolio(models.Model):
    freelancer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='portfolio', limit_choices_to={'user_type': 'freelancer'})
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    experience = models.TextField(blank=True)