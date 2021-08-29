from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Cinema)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['seat_type', 'seat_no', 'row_no', 'cinema']
    list_select_related = ['cinema']


@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    list_select_related = ['cinema', 'movie']
    list_display = ['cinema', 'movie', 'date', 'start_time', 'available']


@admin.register(SeatMapping)
class SeatMappingAdmin(admin.ModelAdmin):
    list_display = ['screening', 'seat', 'price', 'booked']
    list_select_related = ['screening', 'seat']


@admin.register(Booking)
class Booking(admin.ModelAdmin):
    pass
