from .views import index, detail, clear
from django.urls import path

app_name = 'sqlmiddleware'

urlpatterns = [
    path("", index),
    path("<uuid:id>/", detail, name="detail"),
    path("clear/", clear, name="clear"),
]
