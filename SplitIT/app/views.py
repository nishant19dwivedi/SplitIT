from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "home.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        fname = request.POST.get("first-name")
        lname = request.POST.get("last-name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=email).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, "signup.html")
        new_user = User.objects.create_user(
            username=email,
            password=password,
            email=email,
            first_name=fname,
            last_name=lname,
        )
        new_user.save()
        messages.success(request, "Your account has been created successfully.")
        return redirect("login")

    return render(request, "signup.html")
