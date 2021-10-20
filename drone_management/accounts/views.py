from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_pass = request.POST["confirm_pass"]

        if password == confirm_pass:
            if User.objects.filter(username=username).exists():
                print("Username already exists! Please try another one.")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    print("Email address is already taken! Please try another one.")
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect("login")

        else:
            print("Provided passwords did not match! Please try again.")
            return redirect("register")

    else:
        return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            print("Login was successful!")
            return redirect("show_drones")
        else:
            print("Username or password is not correct.")
            return redirect("login")
    else:
        return render(request, "accounts/login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        print("You are logged out from the website.")
        return redirect("login")
