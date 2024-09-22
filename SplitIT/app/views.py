from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Group, GroupMember, Expense, ExpenseShare, Settle, Profile


# Create your views here.
def home(request):
    return render(request, "home.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html")

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


@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard.html")


@login_required(login_url="login")
def profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        profile.about = request.POST.get("about", profile.about)
        profile.gender = request.POST.get("gender", profile.gender)
        profile.save()
        return redirect("profile")  # Redirect to the profile page after updating

    context = {
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "about": profile.about,
        "gender": profile.gender,
    }
    return render(request, "profile.html", context)


def aboutus(request):
    return render(request, "aboutus.html")


def logout(request):
    auth_logout(request)
    return redirect("login")
