from django.contrib import admin
from django.urls import path, include
from .views import Home
from .views import UserListCreateView, UserRetrieveUpdateDestroyView

from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', Home.as_view()),

    path('get_users/', UserListCreateView.as_view(), name='user-list-create'),                 # GET for list, POST for create
    path('get_users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),  # GET, PUT, DELETE for specific user

    path('', include(router.urls)),

]