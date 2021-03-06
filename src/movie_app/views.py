from django.contrib.auth.models import User
from django.db import DatabaseError
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated

from . import models, serializers

# Create your views here.
"""
/* Copyright (C) - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 * Written by Nilanjan Bala <nilanjan1@tutanota.com>, August 2021
 */
"""


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


@api_view(http_method_names=['GET'])
def get_movies(request):
    try:
        city = int(request.query_params['city_val'])
        movies = models.Movie.objects.filter(cinema__city=city)
        ser_movies = serializers.MovieSerializer(movies, many=True)
        return JsonResponse(ser_movies.data, safe=False)
    except KeyError as ke:
        print(ke)
        return JsonResponse({"error": "city value not sent"}, status=500)
    except Exception as ex:
        print(ex)
        return JsonResponse({"error": "Server Error"}, status=500)


@api_view(http_method_names=['GET'])
def get_cinemas(request):
    try:
        movie = int(request.query_params['movie_val'])
        city = request.query_params.get("city_val", "")
        screening = models.Screening.objects.filter(movie=movie)

        if city:
            screening = screening.filter(cinema__city=city)
        ser_screening = serializers.ScreeningSerializer(screening, many=True)
        return JsonResponse(ser_screening.data, safe=False)
    except KeyError as ke:
        print(ke)
        return JsonResponse({"error": "movie value not sent"}, status=500)
    except Exception as ex:
        print(ex)
        return JsonResponse({"error": "Server Error"}, status=500)


@api_view(http_method_names=['GET'])
def get_seats(request):
    try:
        screening = int(request.query_params['screening_val'])
        seats = models.SeatMapping.objects.filter(screening=screening)
        ser_seats = serializers.SeatMappingSerializer(seats, many=True)
        return JsonResponse(ser_seats.data, safe=False)
    except KeyError as ke:
        print(ke)
        return JsonResponse({"error": "screening value not present"},
                            status=500)
    except Exception as ex:
        print(ex)
        return JsonResponse({"error": "Server Error"}, status=500)


@api_view(http_method_names=['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def book_ticket(request):
    try:
        seats = [int(x) for x in request.data["seats"]]
        models.SeatMapping.objects.book_tickets(seats, request.user)
        return JsonResponse({"success": "booked_tickets"})
    except DatabaseError as de:
        print(de)
        return JsonResponse(
            {
                "error":
                "Sorry, some of the seats are already booked, please try again"
            },
            status=500)
    except ValueError as ve:
        print(ve)
        return JsonResponse(
            {"error": "Please choose tickets which are not booked"},
            status=500)
    except Exception as ex:
        print(ex)
        return JsonResponse({"error": "Server Error"}, status=500)
