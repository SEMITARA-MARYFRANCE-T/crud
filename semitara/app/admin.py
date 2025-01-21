from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import LaundryBooking

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']  # Fields to use for autocomplete
    
