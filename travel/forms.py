from django import forms
from django.contrib.auth.models import User
from .models import Profile, Booking, TravelOption
from django.db import transaction

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta: model = User; fields = ["username","email","password"]

class ProfileForm(forms.ModelForm):
    class Meta: model = Profile; fields = ["phone","city"]

class BookingForm(forms.ModelForm):
    class Meta: model = Booking; fields = ["seats"]
    def __init__(self, *args, travel_option:TravelOption, user, **kwargs):
        super().__init__(*args, **kwargs)
        self.travel_option = travel_option
        self.user = user
    def clean_seats(self):
        seats = self.cleaned_data["seats"]
        if seats <= 0: raise forms.ValidationError("Seats must be positive.")
        if seats > self.travel_option.available_seats:
            raise forms.ValidationError("Not enough seats available.")
        return seats
    @transaction.atomic
    def save(self, commit=True):
        seats = self.cleaned_data["seats"]
        topt = TravelOption.objects.select_for_update().get(pk=self.travel_option.pk)
        if seats > topt.available_seats:
            raise forms.ValidationError("Seats just sold out. Try fewer.")
        topt.available_seats -= seats; topt.save(update_fields=["available_seats"])
        booking = Booking(
            user=self.user,
            travel_option=topt,
            seats=seats,
            total_price=seats * topt.price,
        )
        if commit: booking.save()
        return booking
