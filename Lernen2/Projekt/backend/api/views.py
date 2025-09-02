from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Tasks': '/api/tasks/',
        'Admin': '/admin/',
    }
    return Response(api_urls)
