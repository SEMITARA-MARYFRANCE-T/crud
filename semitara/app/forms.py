from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, LaundryBooking, Contact

# Custom User Creation Form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'address', 'age', 'name', 'birthdate')

# Custom User Change Form
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'address', 'age', 'name', 'birthdate')

# Laundry Booking Form
class LaundryBookingForm(forms.ModelForm):
    class Meta:
        model = LaundryBooking
        fields = ('description', 'note', 'weight_kg', 'date', 'status')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

# Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
