from penonton.views import *
from django.urls import path

app_name = "penonton"

urlpatterns = [
    path("", index, name="index"),
    path("waktu/", listWaktuStadium, name="waktu"),
    path("pertandinganStadium/", listPertandinganStadium, name="pertandinganStadium"),
    path("tiket/", tiketPertandingan, name="tiket"),
    path("semuaPertandingan/", listSemuaPertandingan, name="semuaPertandingan"),
]
