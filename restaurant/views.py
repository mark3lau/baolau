from django.shortcuts import render

# Create your views here.

def get_make_reservation(request):
    return render(request, 'reservation/make_reservation.html')