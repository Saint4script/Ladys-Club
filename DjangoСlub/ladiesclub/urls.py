from django.urls import path
from ladiesclub.views import show_main_page, send_form

urlpatterns = [
    path('', show_main_page, name = "main"),
    path('send_form/', send_form, name = "form"),
    path('buuj8gpu3ztysvzodbq88jce733fly.html', fb_verification, name="fb_verification")
]
