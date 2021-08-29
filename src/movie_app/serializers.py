from rest_framework import serializers

from . import models


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = "__all__"


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cinema
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ['id', 'name', 'duration', 'release_date']


class ScreeningSerializer(serializers.ModelSerializer):
    cinema = serializers.StringRelatedField()
    movie = serializers.StringRelatedField()

    class Meta:
        model = models.Screening
        fields = "__all__"


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seat
        fields = ['id', 'seat_no', 'seat_type', 'row_no']


class SeatMappingSerializer(serializers.ModelSerializer):
    seat = SeatSerializer()

    class Meta:
        model = models.SeatMapping
        fields = ['price', 'booked', 'seat']
