from django.db import models
from datetime import datetime



class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)
    
    

    def __str__(self):
        return f"{self.brand} {self.model}"

class CarRental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pickup_date = models.DateField()
    delivery_date = models.DateField()
    rental_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        rental_days = (self.delivery_date - self.pickup_date).days + 1
        self.rental_price = self.car.rental_price * rental_days
        super(CarRental, self).save(*args, **kwargs)

    def __str__(self):
        return f"Rental of {self.car.brand} {self.car.model} from {self.pickup_date} to {self.delivery_date}"
