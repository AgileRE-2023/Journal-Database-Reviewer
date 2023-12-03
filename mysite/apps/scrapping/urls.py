from django.urls import path
from . import views

# ... your other URL patterns ...


urlpatterns = [
    path("reviewer", view=views.index, name="reviewer_scrapping"),
    path("journal", view=views.scraping_jurnal, name="journal_scrapping"),
]