from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *
from .serializers import *

@api_view(["GET", "POST"])
def test(request):
    if request.method == "GET":
        snippet = Book.objects.all()
        serializer = BookSerializer(snippet, many=True)
        return Response(serializer.data, status=200)
    elif request.method == "POST":
        return Response(serializer.errors, status=400)
