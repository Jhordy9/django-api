from api import views
from django.urls import path

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>', views.book_by_pk, name='book_by_pk'),
    path('books/add', views.add_book, name='add_book'),
    path('members/', views.member_list, name='member_list'),
    path('members/<int:pk>', views.member_by_pk, name='member_by_pk'),
    path('members/add', views.add_member, name='add_member'),
    path('loans/', views.loan_list, name='loan_list'),
    path('loans/<int:pk>', views.loan_by_pk, name='loan_by_pk'),
    path('loans/add', views.add_loan, name='add_loan')
]
