from django.shortcuts import render
import requests
from decouple import config
# Create your views here.
def index(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city="kathmandu"
    API_KEY = config("WEATHER_API_KEY")
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    data=requests.get(url).json()
    temp= data['main']['temp']
    # temp_celious=round(temp-273.15)
    desc=data['weather'][0]['description']
    windsp=data['wind']['speed']
    humid=data['main']['humidity']
    pressure=data['main']['pressure']
    visible=data['visibility']
    context={'temp':temp,
             'city':city,
             'desc':desc,
             'windsp':windsp,
             'humid':humid,
             'pressure':pressure,
             'visible':visible
             }
    return render(request,'core/index.html',context)