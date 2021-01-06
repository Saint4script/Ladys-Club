from django.shortcuts import render
from django.http import JsonResponse

def show_main_page(request):
    return render(request, 'index.html')