from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

# Create your views here.


def get_reservation_list(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservation/reservation_list.html', context)


def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_reservation_list')
    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'reservation/make_reservation.html', context)

