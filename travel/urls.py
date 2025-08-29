from django.urls import path
from . import views
urlpatterns = [
    path("", views.travel_list, name="list"),
    path("<int:pk>/", views.travel_detail, name="detail"),
    path("<int:pk>/book/", views.book, name="book"),
    path("bookings/", views.my_bookings, name="bookings"),
    path("booking/<int:pk>/cancel/", views.cancel_booking, name="cancel"),
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
]
