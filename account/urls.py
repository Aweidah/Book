from django.contrib import admin
from django.urls import path
from .views import Home
from .views import UserListCreateView, UserRetrieveUpdateDestroyView


urlpatterns = [
    path('', Home.as_view()),

    path('users/', UserListCreateView.as_view(), name='user-list-create'),                 # GET for list, POST for create
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),  # GET, PUT, DELETE for specific user

]