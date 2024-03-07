from django.shortcuts import render, redirect
from .models import Service, Order, StatusOrder
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from telebot.sendmessage import send_telegram
from .forms import OrderForm, RecordForm


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        sms = request.POST['sms']
        element = Order(order_name=name, order_phone=phone, order_text=sms)
        element.save()
        send_telegram(tg_name=name, tg_phone=phone, tg_sms=sms)
        return render(request, "service/thanks.html", {"name": name})
    else:
        return render(request, "service/thanks.html")


def telegram(request):
    form = OrderForm()

    return render(request, 'service/tg.html', {'form': form})


def index(request):
    projects = Service.objects.all()
    return render(request, 'service/index.html', {'projects': projects})


def home(request):
    return render(request, 'service/home.html')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def worker(request):
    return render(request, 'service/worker.html')


def reguser(request):
    if request.method == 'GET':
        return render(request, 'service/reguser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('worker')
            except IntegrityError:
                return render(request, 'service/reguser.html', {'form': UserCreationForm(),
                                                                'error': 'Такое имя пользователя существует, создайте новое'})
        else:
            return render(request, 'service/reguser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'service/loginuser.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'service/loginuser.html', {
                'form': AuthenticationForm,
                'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('worker')


def map(request):
    return render(request, 'service/map.html')


def record(request):
    form = RecordForm()

    return render(request, 'service/worker.html', {'form': form})
