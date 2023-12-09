from django.db import models


class User(models.Model):
    card_name = models.CharField(max_length=20)
    card_num = models.PositiveBigIntegerField()
    card_period = models.PositiveIntegerField()
    card_cvv = models.PositiveIntegerField()
    rights = models.IntegerField()
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    park_id = models.IntegerField(default=-1)
    

class Parking(models.Model):
    address = models.CharField(max_length=120, default='')
    registry_nubmer = models.PositiveIntegerField(default=9999)
    max_parking_spaces = models.PositiveIntegerField(default=9999)
    occupied_places = models.PositiveIntegerField(default=9999)
    price_per_minute = models.PositiveIntegerField(default=9999)
    free_time = models.PositiveIntegerField(default=40)


class Reciept(models.Model):
    parking_id = models.ForeignKey(Parking, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    benefit = models.BooleanField(default=False)

