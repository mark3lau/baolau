from django.shortcuts import render, redirect
from .models import Reservation

# Create your views here.


def get_reservation_list(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservation/reservation_list.html', context)


def make_reservation(request):
    if request.method == 'POST':
        name = request.POST.get('add_name')
        date = request.POST.get('add_date')
        time = request.POST.get('add_time')
        number_of_people = request.POST.get('add_people')
        Reservation.objects.create(name=name, date=date, time=time, number_of_people=number_of_people)

        return redirect('get_reservation_list')
    return render(request, 'reservation/make_reservation.html')

