from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list books"),
    path('<int:bookId>/', views.viewbook, name="books.view one book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
]