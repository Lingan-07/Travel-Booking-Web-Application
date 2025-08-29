from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from travel.models import TravelOption

class Command(BaseCommand):
    help = "Seed database with sample travel options"

    def handle(self, *args, **kwargs):
        TravelOption.objects.all().delete()  # clear old data

        now = timezone.now()
        samples = [
            ("AI101", "FLIGHT", "Chennai", "Delhi", now + timedelta(days=1, hours=3), 4500, 30),
            ("TR204", "TRAIN", "Mumbai", "Pune", now + timedelta(days=2, hours=1), 600, 120),
            ("BS330", "BUS", "Bangalore", "Hyderabad", now + timedelta(days=1, hours=8), 1200, 40),
        ]

        for tid, t, s, d, dep, price, seats in samples:
            TravelOption.objects.create(
                travel_id=tid,
                type=t,
                source=s,
                destination=d,
                departure=dep,
                price=price,
                available_seats=seats,
            )

        self.stdout.write(self.style.SUCCESS("Sample travel options added!"))
