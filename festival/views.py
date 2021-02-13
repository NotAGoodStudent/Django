from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View


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

