from django.shortcuts import render, redirect, get_object_or_404
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


def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('get_reservation_list')
    form = ReservationForm(instance=reservation)
    context = {
        'form': form
    }
    return render(request, 'restaurant/edit_reservation.html', context)