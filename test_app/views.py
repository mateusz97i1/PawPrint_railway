from django.shortcuts import render
from datetime import datetime
from decouple import config 
import ipdata
# Create your views here.

def getCountryLocation():

    ipdata.api_key=config('IP_DATA')
    ipdata.endpoint="https://eu-api.ipdata.co"

    response=ipdata.lookup()
    countryLocation=response['country_name']


    return countryLocation


def home(request):

    countryLocation=getCountryLocation


    clock=datetime.now()
    current=clock.strftime("%d %B %Y, %H:%M")
   

    context={
        'clock':clock,
        'curr':current,
        'response':countryLocation

    }

    return render(request,'home.html',context)


