from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view

from . import models, serializers

# Create your views here.


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
