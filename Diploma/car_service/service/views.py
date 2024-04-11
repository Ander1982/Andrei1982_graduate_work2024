from django.shortcuts import render, redirect
from .models import Service, Order, Staff, Rec
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from telebot.sendmessage import send_telegram
from .forms import OrderForm, ReviewForm
from django.contrib import messages
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required


def recording(request):
    all_time = ['08:00', '09:00', '10:00', '11:00', '12:00', '14:00', '15:00', '16:00', '17:00']
    date = datetime.today()
    yesterday = date + timedelta(days=1)
    min_day_value = yesterday.strftime('%Y-%m-%d')
    # services = ['Замена масла', 'Ремонт электрооборудования', 'Ремонт ходовой части', 'Шиномонтаж', 'Кузовной ремонт']

    if request.GET.get('date') is None:
        content = {
            # 'services': services,
            'min_day_value': min_day_value,
            'all_time': all_time,
            'step_1': True,
            'step': "Шаг первый"
        }
        return render(request, 'service/recording.html', content)
    else:
        appointment = Rec.objects.filter(rec_day=request.GET.get('date')).all()
        for obj in appointment:
            all_time.remove(obj.rec_time.strftime('%H:%M'))
        content = {
            'min_day_value': min_day_value,
            'all_time': all_time,
            'step_1': False,
            'step_2': True,
            'step': "Шаг второй",
            'choised_day': request.GET.get('date')
        }
        return render(request, 'service/recording.html', content)


def time_recording(request):
    if request.POST:
        name = request.POST['name']
        day = request.POST['date']
        time = request.POST['time']
        element = Rec(rec_name=name, rec_day=day, rec_time=time)
        element.save()

        return render(request, "service/time.html", {'name': name, 'day': day, 'time': time})
    else:
        return render(request, "service/time.html")


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
    st = Staff.objects.all()
    context = {
        'staff': st
    }

    return render(request, 'service/worker.html', context)


@login_required(login_url='login')
def personal(request, pk):
    personal_obj = Staff.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.staff = personal_obj

        review.save()

        personal_obj.get_vote_count()

        messages.success(request, 'Ваш отзыв успешно отправлен!')
        return redirect('personal', pk=personal_obj.id)

    content = {
        'personal': personal_obj,
        'form': form
    }
    return render(request, 'service/personal.html', content)


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

# def record(request):
#     form = RecordForm()
#
#     return render(request, 'service/worker.html', {'form': form})

# def recording(request):
# all_time = ['08:00', '09:00', '10:00', '11:00', '12:00', '14:00', '15:00', '16:00', '17:00']
# yesterday = datetime.today()
# min_day_value = yesterday.strftime('%Y-%m-%d')

# form = RecordingForm()
#
#
# if request.method == 'POST':
#     form = RecordingForm(request.POST)
#     if form.is_valid():
#         form.save()
#
#         messages.success(request, 'Ваш отзыв успешно отправлен!')
#     return redirect(request, 'index')
#
# content = {
#     'form': form,
#
# }
# return render(request, 'service/recording.html', content)
