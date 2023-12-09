from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    card_number = models.PositiveBigIntegerField(max_length=16)
    cvv = models.PositiveIntegerField(max_length=3)
    validity_period = models.PositiveIntegerField(max_length=4)
    rights = models.CharField(max_length=20)


class Parking(models.Model):
    address = models.CharField(max_lenght=120)
    registry_nubmer = models.PositiveIntegerField()
    max_parking_spaces = models.PositiveIntegerField()
    occupied_places = models.PositiveIntegerField()
    price_per_minute = models.PositiveIntegerField()
    free_time = models.PositiveIntegerField()


class Reciept(models.Model):
    parking_id = models.ForeignKey(Parking, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    benefit = models.BooleanField(default=False)

