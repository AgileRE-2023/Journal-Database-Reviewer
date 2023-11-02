from django.urls import path
from . import views

#Tambah URL Route disini
app_name = "reviewer"

urlpatterns = [
    path("", view=views.submission, name='submission'),
    path("upload", view=views.upload, name='upload'),
    path("recommend", view=views.recommend, name='recommend')
]