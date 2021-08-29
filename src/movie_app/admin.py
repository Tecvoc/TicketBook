from django.contrib import admin

#  Proprietary and confidential
#  Written by Nilanjan Bala <nilanjan1@tutanota.com>, August 2021
# Copyright (C) Nilanjan - All Rights Reserved
"""
# Unauthorized copying of this file, via any medium is strictly prohibited
"""

from . import models

# Register your models here.


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Cinema)
class CinemaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['seat_type', 'seat_no', 'row_no', 'cinema']
    list_select_related = ['cinema']


@admin.register(models.Screening)
class ScreeningAdmin(admin.ModelAdmin):
    list_select_related = ['cinema', 'movie']
    list_display = ['cinema', 'movie', 'date', 'start_time', 'available']


@admin.register(models.SeatMapping)
class SeatMappingAdmin(admin.ModelAdmin):
    list_display = ['screening', 'seat', 'price', 'booked']
    list_select_related = ['screening', 'seat']


@admin.register(models.Booking)
class Booking(admin.ModelAdmin):
    pass


# nilanjan
