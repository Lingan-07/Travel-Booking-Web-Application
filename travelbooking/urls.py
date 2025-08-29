from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), # login/logout/password
    path("", RedirectView.as_view(pattern_name="travel:list", permanent=False)),
    path("travel/", include(("travel.urls","travel"), namespace="travel")),
]
