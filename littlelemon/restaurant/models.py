from django.db import models


class MenuItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    description = models.CharField(max_length=250)
    images = models.ImageField(upload_to="restaurant/static/images")
    image_path = models.CharField(max_length=255)


class Book(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identification_number = models.PositiveIntegerField()
    phone_number = models.PositiveIntegerField()
    guests = models.PositiveIntegerField()
    reservation_date = models.CharField(max_length=50)
    reservation_time = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Booking: {self.reservation_date} - {self.reservation_time}"


class Recomendation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
