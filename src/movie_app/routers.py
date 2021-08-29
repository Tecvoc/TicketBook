from django.urls import include, path
from rest_framework.routers import DefaultRouter

"""
#  Written by Nilanjan Bala <nilanjan1@tutanota.com>, August 2021
#  Written by Nilanjan Bala <nilanjan1@tutanota.com>, August 2021
/* Copyright (C) - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 * Proprietary and confidential
"""

from . import views

router = DefaultRouter()
router.register(r'city', views.CityViewSet)
