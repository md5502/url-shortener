from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import path

from .views import UrlView

app_name = "api"


urlpatterns = [
    path("<short_url>/", UrlView.as_view(), name="UrlView"),
    *debug_toolbar_urls(),
]
