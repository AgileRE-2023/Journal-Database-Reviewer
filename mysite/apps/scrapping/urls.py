from django.urls import path
from . import views

# ... your other URL patterns ...


urlpatterns = [
    path("scrape-journals/", view=views.scraping_jurnal, name="dashboard")
]