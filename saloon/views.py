from django.shortcuts import redirect
from django.shortcuts import render
from .forms import BookingModelForm
from .models import Booking
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required 


from django.contrib.auth.models import Group

# from django.contrib.auth.models import Group

# from django.shortcuts import render, redirect
# from django.contrib.auth.models import Group
from django.contrib import messages

from .forms import RegisterForm

from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import Booking

from .serializers import BookingSerializer
from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from rest_framework.decorators import api_view

from rest_framework.response import Response

def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            # Create User
            user = form.save()

            # Get or Create Customer Group
            customer_group, created = Group.objects.get_or_create(
                name="Customer"
            )

            # Assign User to Customer Group
            user.groups.add(customer_group)

            messages.success(
                request,
                "Registration successful. Please login."
            )

            return redirect("login")

        else:

            messages.error(
                request,
                "Please correct the errors below."
            )

    else:

        form = RegisterForm()

    return render(
        request,
        "saloon/register.html",
        {
            "form": form
        }
    )


def user_login(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect(
                "home"
            )

    return render(
        request,
        "saloon/login.html"
    )



@api_view(["POST"])
def api_login(request):

    username = request.data.get(
        "username"
    )

    password = request.data.get(
        "password"
    )

    user = authenticate(
        username=username,
        password=password
    )

    if user:

        token, created = Token.objects.get_or_create(
            user=user
        )

        return Response({

            "token": token.key

        })

    return Response({

        "error": "Invalid Credentials"

    })


# @login_required
def home(request):

    return render(
        request,
        "saloon/home.html"
    )
@login_required
def book_service(request):

    if request.method == "POST":

        form = BookingModelForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            print(
                "Booking Saved"
            )

    else:

        form = BookingModelForm()

    return render(
        request,
        "saloon/booking.html",
        {
            "form": form
        }
    )

# from .models import Booking
@login_required
def booking_list(request):

    if request.user.groups.filter(
        name="Receptionist"
    ).exists():

        bookings = Booking.objects.all()

    else:

        bookings = Booking.objects.filter(
            user=request.user
        )

    return render(
        request,
        "saloon/booking_list.html",
        {
            "bookings": bookings
        }
    )


@login_required
def update_booking(
    request,
    booking_id
):

    booking = Booking.objects.get(
        id=booking_id
    )

    if request.method == "POST":

        form = BookingModelForm(
            request.POST,
            instance=booking
        )

        if form.is_valid():

            form.save()

    else:

        form = BookingModelForm(
            instance=booking
        )

    return render(
        request,
        "saloon/booking.html",
        {
            "form": form
        }
    )

@login_required

def delete_booking(
    request,
    booking_id
):

    booking = Booking.objects.get(
        id=booking_id
    )

    booking.delete()

    return redirect(
        "booking_list"
    )


from django.contrib.auth import logout
# @login_required
def user_Logout(request):

    logout(request)

    return redirect("home")


# from django.contrib.auth.decorators import login_required

@login_required
def customer_dashboard(request):

    return render(
        request,
        "saloon/customer_dashboard.html"
    )


@login_required
def manager_dashboard(request):

    if request.user.groups.filter(
        name="Manager"
    ).exists():

        return render(
            request,
            "saloon/manager_dashboard.html"
        )

    return HttpResponse(
        "Permission Denied"
    )

class BookingViewSet(
    viewsets.ModelViewSet
):

    serializer_class = BookingSerializer

    def get_queryset(self):

        user = self.request.user

        if user.groups.filter(
            name="Receptionist"
        ).exists():

            return Booking.objects.all()

        if user.groups.filter(
            name="Manager"
        ).exists():

            return Booking.objects.all()

        return Booking.objects.filter(
            customer_name=user.username
        )

    def perform_create(
        self,
        serializer
    ):

        serializer.save(
            customer_name=
            self.request.user.username
        )