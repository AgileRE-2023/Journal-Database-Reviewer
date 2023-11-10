from django.urls import path, include
from . import views

# ... your other URL patterns ...


urlpatterns = [
    path("", view=views.index, name="landing"),
    path("signin/", view=views.signin, name="signin"),
    path("dashboard/", view=views.dashboard, name="dashboard"),
    path("upload-ojs/", views.inputDataOJSFile, name="upload data OJS"),
]
