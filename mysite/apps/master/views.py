# from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import EditorForm


# Create your views here.
def index(request):
    return render(request, "master/landing.html")


def signin(request):
    if request.method == "POST":
        form = EditorForm(data=request.POST)
        email = form.data["email"]
        password = form.data["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(
                request,
                "master/signin.html",
                {"form": form, "error": "User not found"},
            )
    else:
        form = EditorForm()

    return render(request, "master/signin.html", {"form": EditorForm()})


def csrf_failure(request, reason=""):
    if request.method == "POST":
        form = EditorForm(data=request.POST)
        email = form.data["email"]
        password = form.data["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(
                request,
                "master/signin.html",
                {"form": form, "error": "User not found"},
            )
    else:
        form = EditorForm()
    return render(request, "master/signin.html", {"form": EditorForm()})


def dashboard(request):
    return render(request, "master/dashboard.html")
