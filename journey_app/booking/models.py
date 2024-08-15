from django.db import models

# Create your models here.



class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

class Trajet(models.Model):
    id_trajet = models.AutoField(primary_key=True)
    #trajet_initial_posix
    #trajet_destination_posix
    trajet_with_escale = models.BooleanField(default=True)
    nombre_escale = models.IntegerField()
    #escales_nameposix (tuples (nom, (x,y,z)))
    id_compagnie = models.ForeignKey("Compagnie",  on_delete=models.CASCADE)

class Vehicule(models.Model):
    matricule_vehicule = models.IntegerField(primary_key=True) 
    marque_vehicule = models.CharField(max_length = 50)
    owner_name = models.CharField(max_length = 50)
    type_vehicule = models.CharField(max_length=20) #moto, voiture, tricycle,bus ......
    default_places = models.IntegerField()
    availables_places = models.IntegerField()
    is_available = False if availables_places == 0 else True # je ferai en for que available_places ne soit jamais negatif
    id_conducteur = models.ForeignKey("Conducteur",  on_delete=models.CASCADE)

class Conducteur(models.Model):
    id_conducteur = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    is_available  = models.BooleanField(default=True)




class Compagnie(models.Model):
    id_compagnie = models.AutoField(primary_key=True)
    name_compagnie = models.CharField(max_length=50)
    email_compagnie = models.CharField(max_length=50)    


LES_TYPES_DE_VEHICULES = {
    "V": "Voiture",
    "M": "Moto",
    "T": "Tricycle",
    "B": "Bus"
}

class Booking(models.Model):
    id_booking = models.AutoField(primary_key=True)
    #booking_initial_posix
    #booking_destination_posix
    booking_with_escale = models.BooleanField(default=True)
    places_reservees = models.IntegerField()
    booked_vehicles = models.CharField(max_length=1, choices=LES_TYPES_DE_VEHICULES)
