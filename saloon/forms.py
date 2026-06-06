from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Booking

class RegisterForm(UserCreationForm):

    class Meta:

        model = get_user_model()

        fields = (
            "email",
            "password1",
            "password2"
        )



class BookingModelForm(ModelForm):

    class Meta:

        model = Booking

        fields = [
            "customer_name",
            "service",
            "booking_date",
            "booking_time"
        ]