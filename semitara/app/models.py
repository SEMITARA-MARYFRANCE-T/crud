from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Additional fields for the user model
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)  # Age field
    name = models.CharField(max_length=255, blank=True)  # Full name field
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

class LaundryBooking(models.Model):
    # Relating the booking to a user
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    description = models.TextField()  # Description of the laundry items
    note = models.TextField(blank=True)  # Optional note for suggestions
    weight_kg = models.PositiveIntegerField()  # Weight in kilograms
    date = models.DateField()  # Date for the booking/schedule
    status_choices = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

    def __str__(self):
        return f"{self.user.username}'s laundry booking on {self.date}"

    class Meta:
        verbose_name = 'Laundry Booking'
        verbose_name_plural = 'Laundry Bookings'
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"