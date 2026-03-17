from django.shortcuts import render
import requests
from decouple import config
from django.contrib import messages
# Create your views here.
def index(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city="kathmandu"
    API_KEY = config("WEATHER_API_KEY")
    UNSPLASH_API_KEY = config("UNSPLASH_API_KEY")
    
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    data=requests.get(url).json()
    img_url=f'https://api.unsplash.com/search/photos?query={city}&per_page=1&client_id={UNSPLASH_API_KEY}'
    response=requests.get(img_url).json()
  
    try:
        temp= data['main']['temp']
        # temp_celious=round(temp-273.15)
        desc=data['weather'][0]['description']
        windsp=data['wind']['speed']
        humid=data['main']['humidity']
        pressure=data['main']['pressure']
        visible=data['visibility']
        feel=data['main']['feels_like']
        image= response['results'][0]['urls']['regular']
        context={'temp':temp,
                'city':city,
                'desc':desc,
                'windsp':windsp,
                'humid':humid,
                'pressure':pressure,
                'visible':visible,
                'feel':feel,
                'image':image
                }
        return render(request,'core/index.html',context)
    except:
        messages.error(request,'No such city!!!')
        temp= 0
        # temp_celious=round(temp-273.15)
        desc="No city"
        windsp=0
        humid=0
        pressure=0
        visible=0
        image="No image available"
        context={'temp':temp,
                'city':city,
                'desc':desc,
                'windsp':windsp,
                'humid':humid,
                'pressure':pressure,
                'visible':visible
                }
        return render(request,'core/index.html',context)
        