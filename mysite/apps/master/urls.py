from django.contrib.auth.views import LogoutView
from django.urls import path, include
from mysite.settings import LOGOUT_REDIRECT_URL
from . import views

# ... your other URL patterns ...


urlpatterns = [
    path("", view=views.index, name="landing"),
    path("signin/", view=views.signin, name="signin"),
    path('logout', view=LogoutView.as_view(next_page=LOGOUT_REDIRECT_URL), name='logout'),
    path("upload-ojs/", views.inputDataOJSFile, name="upload data OJS"),
]
