from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='books/')
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title
