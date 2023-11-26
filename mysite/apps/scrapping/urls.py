from django.urls import path, include
from . import views

# ... your other URL patterns ...


urlpatterns = [
    path("reviewer", view=views.reviewerScrapping, name="reviewer_scrapping")
]