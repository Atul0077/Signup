# signupapp/forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    country = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    # password = forms.CharField(widget=forms.PasswordInput, required=True)
    # confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    agree_to_terms = forms.BooleanField(required=True)


confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password', required=True)


class Meta:
    model = User
    fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'country', 'email', 'phone_number', 'password',
              'confirm_password', 'agree_to_terms']


def clean_phone_number(self):
    phone_number = self.cleaned_data['phone_number']
    if not phone_number.isdigit():
        raise ValidationError("Phone number must contain only digits.")
    return phone_number


def clean_confirm_password(self):
    password = self.cleaned_data.get('password')
    confirm_password = self.cleaned_data.get('confirm_password')

    if password and confirm_password and password != confirm_password:
        raise ValidationError("Passwords do not match.")

    return confirm_password
