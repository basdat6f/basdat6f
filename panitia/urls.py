from panitia.views import *
from django.urls import path

app_name = 'panitia'

urlpatterns = [
    path('', index ,name="index"),
    path('mulai/', mulai, name="mulai"),
    path('peristiwa/', peristiwa, name="peristiwa"),
    path('profile/', show_profile, name="profile"),
    path('manage/', manage_pertandingan, name="manage_pertandingan"),
    path('peristiwa/list/', list_peristiwa, name="list_peristiwa"),
    path('buatPertandingan/', buat_pertandingan, name='buatPertandingan'),
    path('listPertandingan/', list_pertandingan, name='listPertandingan'),
    path('mulaiRapat/', mulai_rapat, name='mulaiRapat'),
    path('notaRapat/', nota_rapat, name='notaRapat'),
    path('submitPertandingan/', submit_pertandingan, name='submit_pertandingan'),
    path('scheduleList/', schedule_list, name='scheduleList'),
]
