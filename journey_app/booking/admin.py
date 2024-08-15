from django.contrib import admin
from .models import Conducteur, Client, Vehicule, Compagnie, Trajet, Booking
# Register your models here.
admin.site.register(Conducteur)
admin.site.register(Client)
admin.site.register(Vehicule)
admin.site.register(Compagnie)
admin.site.register(Trajet)
admin.site.register(Booking)