from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import *

def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Reja.objects.create(
                t_name=request.POST.get("t_name"),
                t_datail=request.POST.get("t_datail"),
                sana=request.POST.get("sana"),
                t_status=request.POST.get("t_status"),
                egasi=request.user
            )
            return redirect("/index/")
        content = {
            "rejalar": Reja.objects.filter(egasi=request.user),
            "foydalanuvchi": request.user.username.capitalize()
        }
        return render(request, "index.html", content)
    return redirect("/")

def edit(request):
    return render(request, "edit.html")

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST.get("username"),
            password = request.POST.get("password")
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/index/")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("/")

def delete_reja(request, son):
    Reja.objects.get(id=son).delete()
    return redirect("/index/")