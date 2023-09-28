from django.urls import path
from . import views

#Tambah URL Route disini
urlpatterns = [
    path("", view=views.index, name='index')
]