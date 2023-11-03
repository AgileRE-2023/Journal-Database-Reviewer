from django.urls import path, include
from . import views
# ... your other URL patterns ...


urlpatterns = [
    path("", view=views.index),
    path('input-data-ojs-file/', views.inputDataOJSFile, name='input_data_ojs_file'),
]