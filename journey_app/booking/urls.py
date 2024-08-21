from django.urls import path

from . import views


app_name = "journey_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("booking_page/", views.booking_page, name="booking_page"),
]