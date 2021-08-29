from django.contrib.auth.models import User
from django.db import models

"""
/* Copyright (C) - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 * Proprietary and confidential
"""

#  Written by Nilanjan Bala <nilanjan1@tutanota.com>, August 2021


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cinema(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City,
                             on_delete=models.CASCADE,
                             related_name="cinema")

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    release_date = models.DateField()
    cinema = models.ManyToManyField(Cinema,
                                    through='Screening',
                                    related_name="movies")

    def __str__(self):
        return self.name


class Seat(models.Model):
    seat_no = models.PositiveIntegerField()
    cinema = models.ForeignKey(Cinema,
                               on_delete=models.CASCADE,
                               related_name="cinema_seats")
    seat_type = models.CharField(max_length=100)
    row_no = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cinema.name} - {self.seat_type} seat no {self.seat_no} row {self.row_no}"


class Screening(models.Model):
    cinema = models.ForeignKey(
        Cinema,
        on_delete=models.CASCADE,
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    start_time = models.TimeField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{str(self.movie.name)} in {str(self.cinema.name)} at {self.start_time}"


class SeatMapping(models.Model):
    screening = models.ForeignKey(
        Screening,
        on_delete=models.CASCADE,
    )
    seat = models.ForeignKey(
        Seat,
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    booked = models.BooleanField(default=False)


class Booking(models.Model):
    booking_id = models.OneToOneField(SeatMapping, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name="bookings")
    booking_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
