from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='book_home'),
    path('list/',views.ListBook.as_view(),name='book_list'),
    path('detail/<int:pk>',views.DetailBook.as_view(),name='book_detail'),
    path('create/',views.CreateBook.as_view(),name='book_create'),
    path('update/<int:pk>',views.UpdateBook.as_view(),name='book_update'),
    path('delete/<int:pk>',views.DeleteBook.as_view(),name='book_delete'),
    path('category/<int:pk>',views.book_by_category.as_view(),name='book_category'),
    path('seller/<int:pk>',views.book_by_seller.as_view(),name='book_seller'),
    path('search/',views.search_book.as_view(),name='search_book'),
    path('bookmark/<int:pk>',views.bookmark_book,name='bookmark_book'),
    path('like/<int:pk>',views.like_book,name='like_book'),
    path('show_bookmark/',views.ShowBookmark.as_view(),name='show_bookmark'),
    path('filter_by_price/',views.filter_by_price.as_view(),name='filter_by_price'),
]