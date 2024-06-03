from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import book_list, book_create, book_update, book_delete
from .views import author_list, author_create, author_update, author_delete
from .views import category_list, category_create, category_update, category_delete
from .api_views import BookViewSet, AuthorViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/create/', book_create, name='book_create'),
    path('books/<int:pk>/update/', book_update, name='book_update'),
    path('books/<int:pk>/delete/', book_delete, name='book_delete'),
    path('authors/', author_list, name='author_list'),
    path('authors/create/', author_create, name='author_create'),
    path('authors/<int:pk>/update/', author_update, name='author_update'),
    path('authors/<int:pk>/delete/', author_delete, name='author_delete'),
    path('categories/', category_list, name='category_list'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/<int:pk>/update/', category_update, name='category_update'),
    path('categories/<int:pk>/delete/', category_delete, name='category_delete'),
    path('api/', include(router.urls)),
]
