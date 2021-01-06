from django.urls import path
from .views import show_main_page

urlpatterns = [
    path('', show_main_page, name = "main"),
]