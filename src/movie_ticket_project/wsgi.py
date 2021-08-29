"""
WSGI config for movie_ticket_project project.

/* Copyright (C) - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 * Written by Nilanjan Bala <nilanjan1@tutanota.com>, August 2021
 */
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_ticket_project.settings')

application = get_wsgi_application()
