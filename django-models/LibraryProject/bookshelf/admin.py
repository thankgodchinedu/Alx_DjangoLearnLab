from .models import Book
from django.contrib import admin

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show
    search_fields = ('title', 'author')                     # enable search
    list_filter = ('publication_year',)                    # enable filtering
