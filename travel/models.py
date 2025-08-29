from django.conf import settings
from django.db import models, transaction
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50, blank=True)
    def __str__(self): return f"{self.user.username} Profile"

class TravelOption(models.Model):
    class Type(models.TextChoices):
        FLIGHT="FLIGHT","Flight"; TRAIN="TRAIN","Train"; BUS="BUS","Bus"
    travel_id = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=10, choices=Type.choices)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField(default=0)
    def __str__(self): return f"{self.travel_id} {self.source}->{self.destination}"

class Booking(models.Model):
    class Status(models.TextChoices):
        CONFIRMED="CONFIRMED","Confirmed"; CANCELLED="CANCELLED","Cancelled"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.PROTECT)
    seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    booked_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.CONFIRMED)

    def cancel(self):
        if self.status == self.Status.CONFIRMED:
            with transaction.atomic():
                self.status = self.Status.CANCELLED
                self.save(update_fields=["status"])
                # return seats
                topt = TravelOption.objects.select_for_update().get(pk=self.travel_option_id)
                topt.available_seats += self.seats
                topt.save(update_fields=["available_seats"])

