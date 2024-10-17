from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields = ['id', 'title', 'name', 'author']

class NewBookSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields = "__all__"
