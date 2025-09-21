from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("usefulthings/", include("usefulthings.urls", namespace="usefulthings")),
    path("users/", include("users.urls", namespace="users")),
]
