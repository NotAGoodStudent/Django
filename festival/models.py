from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE

class Tickets(models.Model):
    ticketID = models.AutoField(primary_key=True)
    artistName = models.CharField(max_length=20)
    stock = models.IntegerField()

class Bookings(models.Model):
    bookingID = models.AutoField(primary_key=True)
    booker = models.ForeignKey(User, on_delete=CASCADE)
    bookedTicket = models.ForeignKey(Tickets, on_delete=CASCADE)
    quantity = models.IntegerField()