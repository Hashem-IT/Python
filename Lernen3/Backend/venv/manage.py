#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    from django.core.management import execute_from_command_line
    from django.urls import path
    from django.conf import settings
    from django.http import JsonResponse

    # Einfache URL Konfiguration
    urlpatterns = [
        path('api/', lambda request: JsonResponse({
            'message': 'Hallo von Django!',
            'tasks': [
                {'id': 1, 'title': 'Erste Aufgabe', 'completed': False},
                {'id': 2, 'title': 'Zweite Aufgabe', 'completed': True}
            ]
        }))
    ]

    settings.ROOT_URLCONF = urlpatterns

    execute_from_command_line(sys.argv)
