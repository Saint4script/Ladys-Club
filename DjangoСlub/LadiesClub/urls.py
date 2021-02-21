from django.urls import path
from LadiesClub.views import show_main_page, send_form

urlpatterns = [
    path('', show_main_page, name = "main"),
    path('send_form/', send_form, name = "form")
]
