from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Project, Portfolio

class SignUpForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('company', 'Company'),
        ('freelancer', 'Freelancer'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'budget', 'skills')

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('bio', 'skills', 'experience')