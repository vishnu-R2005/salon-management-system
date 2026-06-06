from django.contrib import admin

# Register your models here.
from .models import Booking

# admin.site.register(Booking)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "customer_name",
        "service",
        "booking_date",
        "booking_time"
    )

    search_fields = (
        "customer_name",
        "service"
    )
    ordering = (
    "-booking_date",
)
    

