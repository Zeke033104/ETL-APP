from django.urls import path
from .views import upload_and_run, success

urlpatterns = [
    path("etl/",     upload_and_run, name="etl"),
    path("success/", success,        name="success"),
]