from rest_framework import serializers
from .models import Booking
from datetime import date, time


class BookingSerializer(serializers.ModelSerializer):

    class Meta:

        model = Booking

        fields = "__all__"

        read_only_fields = (
            "customer_name",
        )

    def validate_booking_date(
        self,
        value
    ):

        if value < date.today():

            raise serializers.ValidationError(
                "Past dates are not allowed."
            )

        return value

    def validate_booking_time(
        self,
        value
    ):

        if value < time(9, 0):

            raise serializers.ValidationError(
                "Salon opens at 9 AM."
            )

        if value > time(20, 0):

            raise serializers.ValidationError(
                "Salon closes at 8 PM."
            )

        return value

    def validate(
        self,
        data
    ):

        exists = Booking.objects.filter(

            customer_name=
            self.context[
                "request"
            ].user.username,

            booking_date=
            data["booking_date"],

            booking_time=
            data["booking_time"]

        ).exists()

        if exists:

            raise serializers.ValidationError(
                "You already have a booking at this time."
            )

        return data