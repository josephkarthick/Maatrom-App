from django.db import models

class Slot(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('booked', 'Booked'),
    ]

    name = models.CharField(max_length=50)
    ph_number = models.CharField(max_length=10)  # Changed to CharField for phone numbers
    date = models.DateField()  # Stores the selected date
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='available')
    notes = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date} - {self.status}"

from django.db import models

class Availability(models.Model):
    date = models.DateField(unique=True)
    status = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.date} - {self.status} ({self.color})"
