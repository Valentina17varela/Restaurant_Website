from django.db import models


class MenuItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    description = models.CharField(max_length=250)
    images = models.ImageField(upload_to="images/")


class Booking(models.Model):
    name = models.CharField(max_length=100)
    guests = models.PositiveIntegerField()
    bookingDate = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.bookingDate}"


class Recomendation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
