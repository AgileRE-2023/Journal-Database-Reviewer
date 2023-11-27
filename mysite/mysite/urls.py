"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.reviewer import views

# ... your other URL patterns ...


urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', views.reviewer_list, name="reviewer_list"),
    # path('add', views.add, name="add"),
    # path('edit/<int:id>', views.edit, name='edit'),
    # path('delete/<int:id>', views.delete, name='delete'),
    path("", include('apps.master.urls')),
    path("reviewer/", include('apps.reviewer.urls')),
    path("scrapping/", include('apps.scrapping.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path("editor/", include('apps.editor.urls')),
]
