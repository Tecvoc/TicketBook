from django.urls import path, include

from . import views
from .routers import router

urlpatterns = [
    path('', include(router.urls)),
    path('movie/', views.get_movies),
    path('cinema/', views.get_cinemas),
    path('seats/', views.get_seats)
]
