
from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_number', 'check_in_date', 'check_out_date', 'guests', 'created_at')  # Adjust as needed
