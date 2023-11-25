from django.urls import path
from . import views

# ... your other URL patterns ...


urlpatterns = [
    path("scraping-jurnal/", views.scraping_jurnal, name="scraping_jurnal"),
]