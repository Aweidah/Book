from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

# Use DRF's views for handling account creation, updating, and deletion.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action


class Home(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

# List and Create Users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Retrieve, Update, and Delete a User by ID
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Retrieve, Update, and Delete
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Custom logic for creating user
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass

    @action(detail=True, methods=['put'])
    def update_account(self, request, pk=None):
        # Custom logic for updating user
        pass

    @action(detail=True, methods=['delete'])
    def delete_account(self, request, pk=None):
        # Custom logic for deleting user
        pass