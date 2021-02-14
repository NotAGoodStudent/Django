from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
from django.views.generic.base import View

from festival.models import Tickets, Bookings


class HelloWorld(View):

    def get(self, request):
        return render(request, 'index.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return self.get(request)

class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('login')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self,request):
        exists = User.objects.filter(username=request.POST['username'], email=request.POST['email']).exists()
        if exists is None:
            passw = request.POST['password']
            passw2 = request.POST['password2']
            if passw == passw2:
                User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'], first_name=request.POST['name'], last_name=request.POST['surname'])
                return redirect('login')

        return redirect('register')

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class TicketView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'addTickets.html')

    def post(self, request):
        exists = Tickets.objects.filter(artistName=request.POST['artistName']).exists()
        if exists is False:
            Tickets.objects.create(artistName=request.POST['artistName'], stock=request.POST['stock'])
            return redirect('ticket')
        else:
            ticket = Tickets.objects.get(artistName=request.POST['artistName'])
            ticket.stock += int(request.POST['stock'])
            ticket.save()
            return redirect('ticket')

class BookingView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'tickets': list(Tickets.objects.all())
        }
        return render(request, 'bookTickets.html', context=context)

    def post(self, request):
        print(request.POST['ticketid'])
        print(request.POST['quantity'])
        ticket = Tickets.objects.get(ticketID=int(request.POST['ticketid']))
        print(ticket.artistName)
        user = request.user
        print(ticket.stock - int(request.POST['quantity']) > 0)
        if ticket.stock - int(request.POST['quantity']) > 0:
            ticket.stock -= int(request.POST['quantity'])
            Bookings.objects.create(booker=user, bookedTicket=ticket, quantity=request.POST['quantity'])
            ticket.save()
            return redirect('book')
        else:
            return redirect('book')

class CheckBookings(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context = \
            {
                'myBookings': list(Bookings.objects.filter(booker=user))

            }
        return render(request, 'myBookings.html', context=context)





