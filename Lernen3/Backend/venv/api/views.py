from django.http import JsonResponse


def api_test(request):
    return JsonResponse({
        'message': 'Hallo von Django!',
        'tasks': [
            {'id': 1, 'title': 'Erste Aufgabe', 'completed': False},
            {'id': 2, 'title': 'Zweite Aufgabe', 'completed': True}
        ]
    })
