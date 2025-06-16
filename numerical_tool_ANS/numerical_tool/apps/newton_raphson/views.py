from django.shortcuts import render

def home(request):
    return render(request, 'newton_raphson/home.html')