from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(
    [Author, Publisher, Store, Piece, Article, Book, BookReview])
