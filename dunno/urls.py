"""dunno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from festival.views import HelloWorld, LoginView, RegisterView, LogoutView, TicketView, BookingView, CheckBookings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HelloWorld.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('createTicket/', TicketView.as_view(), name='ticket'),
    path('book/', BookingView.as_view(), name='book'),
    path('myBookings/', CheckBookings.as_view(), name='myBookings')
]
