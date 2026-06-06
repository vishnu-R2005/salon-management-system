from django.db import models

class Booking(models.Model):

    customer_name = models.CharField(
        max_length=100
    )

    service = models.CharField(
        max_length=100
    )

    booking_date = models.DateField()

    booking_time = models.TimeField()

    def __str__(self):
        return f"{self.user.customer_name} - {self.service}"