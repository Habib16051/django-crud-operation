from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('<int:pk>', views.BookView.as_view(), name='book_view'),
    path('new/', views.BookCreate.as_view(), name='book_new'),
    path('update/<int:pk>', views.BookList.as_view(), name='book_update'),
    path('delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
]
