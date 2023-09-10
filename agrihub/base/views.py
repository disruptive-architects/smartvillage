from django.shortcuts import render, redirect, HttpResponse
import requests

from base.forms import MyForm


# Create your views here.


def home(request):
    return render(request, 'home.html')


def weather(request):
    context = requests.get("http://192.168.1.100:3000/get-weather-data").json()
    return render(request, 'weather.html', context)

def submit_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            from_address = form.cleaned_data['from_address']
            to_address = form.cleaned_data['to_address']
            object_details = form.cleaned_data['object_details']
            phone_number = form.cleaned_data['phone_number']

            # Prepare data to send to the API
            data = {
                'from_address': from_address,
                'to_address': to_address,
                'object_details': object_details,
                'phone_number': phone_number,
            }

            # Define the API endpoint URL
            api_url = 'http://192.168.1.100:4000/add-new-journey'

            # Send a POST request to the API
            response = requests.post(api_url, json=data)

            if response.status_code == 200:
                # Successful API response, you can handle this as needed
                return HttpResponse('success_page')
            else:
                # Handle API errors or bad responses here
                # You can add error messages to the form or log errors
                form.add_error(None, 'Error sending data to API')
    else:
        form = MyForm()

    return render(request, 'transportation.html', {'form': form})


def services(request):
    return render(request, 'service.html')
