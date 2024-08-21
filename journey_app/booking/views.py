from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {
        'welcome_message': "Welcome to the Polls App!",
        'vehicles': LES_TYPES_DE_VEHICULES
    }
    return render(request, 'index.html', context)

def booking_page(request):
    if request.method == "POST":
        # Traitez les données de la réservation ici, par exemple, en créant un nouvel objet Booking
        booking_with_escale = request.POST.get('booking_with_escale')
        places_reservees = request.POST.get('places_reservees')
        booked_vehicles = request.POST.get('booked_vehicles')

        # Pour cet exemple, on renvoie simplement les données, mais vous voudrez probablement les sauvegarder dans la base de données
        return HttpResponse(f"Réservation créée avec succès : {places_reservees} places réservées en {LES_TYPES_DE_VEHICULES[booked_vehicles]} avec escale : {booking_with_escale}")
    return render(request, 'booking_page.html', {"LES_TYPES_DE_VEHICULES": LES_TYPES_DE_VEHICULES})