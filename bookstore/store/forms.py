from django import forms
from .models import Book, Author, Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'image', 'category', 'authors']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
