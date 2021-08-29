from django.urls import include, path

from . import views
from .routers import router

"""
/* Copyright (C) - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 * Proprietary and confidential
 *
"""
"""
 * Written by Nilanjan Bala <nilanjan1@tutanota.com>, August 2021
"""

app_name = "movie_app"

urlpatterns = [
    path('', include(router.urls)),
    path('movie/', views.get_movies),
    path('cinema/', views.get_cinemas),
    path('seats/', views.get_seats),
]
