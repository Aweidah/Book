# from django.contrib import admin
# from .models import *

# admin.site.register(Book)

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Organize fields into fieldsets
    fieldsets = (
        (None, {
            'fields': ('title', 'name', 'author')
        }),
        ('Advanced options', {
            'classes': ('collapse',),  # Collapse section for status
            'fields': ('status',),
        }),
    )

    # Display fields in list view
    list_display = ('id', 'title', 'name', 'author', 'status')

    # Set default values when adding a new Book
    def get_changeform_initial_data(self, request):
        # Set default 'name' to 'matrix' and 'status' to 'archived'
        return {
            'name': 'matrix',
            'status': 'archived',
        }

admin.site.register(Book, BookAdmin)


