from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import LaundryBooking

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']  # Fields to use for autocomplete
    
from django.contrib import admin
from .models import CustomUser, LaundryBooking, Contact



# Register LaundryBooking and Contact models
class LaundryBookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'weight_kg', 'date', 'status']
    list_filter = ['status', 'date']
    search_fields = ['user__username', 'description']
    ordering = ['date']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'replied']
    list_filter = ['replied', 'created_at']
    search_fields = ['name', 'email']
    ordering = ['created_at']


admin.site.register(LaundryBooking, LaundryBookingAdmin)
admin.site.register(Contact, ContactAdmin)
