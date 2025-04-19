from django.contrib import admin
from django.urls import path
from django.urls import include # Add this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")), # Add this line
]