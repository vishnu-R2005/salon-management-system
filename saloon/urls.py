from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register(
    r'api/bookings',
    views.BookingViewSet,
    basename='booking'
)

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'book-service/',
        views.book_service,
        name='book_service'
    ),

    path(
        'bookings/',
        views.booking_list,
        name='booking_list'
    ),

    path(
        'update-booking/<int:booking_id>/',
        views.update_booking,
        name='update_booking'
    ),

    path(
        'delete-booking/<int:booking_id>/',
        views.delete_booking,
        name='delete_booking'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'logout/',
        views.user_Logout,
        name='logout'
    ),

    path(
        'dashboard/',
        views.customer_dashboard,
        name='dashboard'
    ),

    path(
        'manager/',
        views.manager_dashboard,
        name='manager_dashboard'
    ),

] + router.urls