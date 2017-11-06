from django.db import models
from django.db.models import Avg


# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class ThemeBlog(Blog):
    theme = models.CharField(max_length=200)


ThemeBlog


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=300)
    # books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=20)
    data = models.IntegerField()

    class Meta:
        ordering = ['name']


Item


class Piece(models.Model):
    name = models.CharField(max_length=100)
    pass


class Article(Piece):
    article_piece = models.OneToOneField(
        Piece, on_delete=models.CASCADE, parent_link=True)


class Book(Piece):
    book_piece = models.OneToOneField(
        Piece, on_delete=models.CASCADE, parent_link=True)


class BookReview(Book, Article):
    name = models.CharField(max_length=200)
    pass
