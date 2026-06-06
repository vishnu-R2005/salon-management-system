from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class RegisterForm(UserCreationForm):

    class Meta:

        model = CustomUser

        fields = (

            "username",

            "email",

            "phone_number",

            "gender",

            "password1",

            "password2",

        )