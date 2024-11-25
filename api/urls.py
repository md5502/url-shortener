from django.urls import path

from .views import create_url, delete_url, go_to_base_url, list_url, retrieve_url, update_url

app_name = "api"

urlpatterns = [
    path("list", list_url),
    path("create", create_url),
    path("update/<str:short_code>", update_url),
    path("delete/<str:short_code>", delete_url),
    path("<str:short_code>", retrieve_url),
    path("go/<str:short_code>", go_to_base_url),

]
