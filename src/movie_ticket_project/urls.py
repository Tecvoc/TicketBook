"""movie_ticket_project URL Configuration

/* Copyright (C) - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential

 * Written by Nilanjan Bala <nilanjan1@tutanota.com>, August 2021
 */

"""

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movie_app.urls')),
    path('api-token/', views.get_auth_token),
    path('register/', views.signup)
]
