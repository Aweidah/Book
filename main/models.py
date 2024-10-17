from django.db import models

class Book(models.Model):
    STATUS_CHOICES = (
        ('archived', 'Archived'),
        ('published', 'Published'),
        ('draft', 'Draft'),
    )

    title = models.CharField(max_length=255) 
    name = models.CharField(max_length=255, default='matrix')  # Default value for name
    author = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='archived')  # Default status

    def __str__(self):
        return self.title
