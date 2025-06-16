from django.urls import path
from .views import QuoteCreateView, EditView, QuoteDeleteView, AuthorView, main, quotes_by_tag

urlpatterns = [
    path('', main, name='index'),
    path('<int:page>', main, name='index_paginated'),
    path('create/', QuoteCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', QuoteDeleteView.as_view(), name='delete'),
    path("author/<int:pk>/", AuthorView.as_view(), name='author'),
    path("tag/<int:tag_id>/", quotes_by_tag, name='quotes_by_tag'),
]
