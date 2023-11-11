from django.shortcuts import render
import calendar
from datetime import datetime
from .models import *
from datetime import datetime


def home(request):
    return render(request ,'Home.html')

def getcars(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        p_date = request.POST.get('pickupDate')
        d_date = request.POST.get('deliveryDate')
        pickup_date = datetime.strptime(request.POST.get('pickupDate'), '%d-%m-%Y')
        delivery_date = datetime.strptime(request.POST.get('deliveryDate'), '%d-%m-%Y')

        if delivery_date.time() == datetime.min.time():
            delivery_date = delivery_date.replace(hour=23, minute=59, second=59)

        rented_cars = CarRental.objects.filter(
            pickup_date__lte=delivery_date, 
            delivery_date__gte=pickup_date
        ).values_list('car', flat=True)

        available_cars = Car.objects.filter(location=location).exclude(id__in=rented_cars)

        for car in available_cars:
            rental_days = (delivery_date - pickup_date).days + 1
            car.total_price = rental_days * car.rental_price
            
        return render(request, 'cars.html', {
            'available_cars': available_cars,
            'location': location,
            'pickup_date': p_date,
            'delivery_date': d_date,
        })

    return render(request, 'cars.html')