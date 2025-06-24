from django.shortcuts import render

def home(request):
    return render(request, 'newton_raphson/newton_raphson.html')