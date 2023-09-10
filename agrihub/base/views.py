from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def weather(request):
    return render(request, 'weather.html')
