from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.utils import timezone
from .models import TravelOption, Booking, Profile
from .forms import RegisterForm, ProfileForm, BookingForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            messages.success(request, "Welcome!")
            return redirect("travel:list")
    else:
        form = RegisterForm()
    return render(request, "travel/register.html", {"form": form})

@login_required
def profile(request):
    prof = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=prof)
        if form.is_valid():
            form.save(); messages.success(request,"Profile updated")
            return redirect("travel:profile")
    else:
        form = ProfileForm(instance=prof)
    return render(request, "travel/profile.html", {"form": form})

def travel_list(request):
    qs = TravelOption.objects.all().order_by("departure")
    t = request.GET.get("type"); s = request.GET.get("source"); d = request.GET.get("dest"); date = request.GET.get("date")
    if t: qs = qs.filter(type=t)
    if s: qs = qs.filter(source__icontains=s)
    if d: qs = qs.filter(destination__icontains=d)
    if date: qs = qs.filter(departure__date=date)
    return render(request, "travel/list.html", {"items": qs, "q": request.GET})

def travel_detail(request, pk):
    item = get_object_or_404(TravelOption, pk=pk)
    return render(request, "travel/detail.html", {"item": item})

@login_required
def book(request, pk):
    item = get_object_or_404(TravelOption, pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST, travel_option=item, user=request.user)
        if form.is_valid():
            booking = form.save()
            messages.success(request, "Booking confirmed.")
            return redirect("travel:bookings")
    else:
        form = BookingForm(travel_option=item, user=request.user)
    return render(request, "travel/book.html", {"item": item, "form": form})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by("-booked_at")
    return render(request, "travel/bookings.html", {"bookings": bookings})

@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if booking.status == Booking.Status.CONFIRMED:
        booking.cancel()
        messages.info(request, "Booking cancelled.")
    return redirect("travel:bookings")

