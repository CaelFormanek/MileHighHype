from django.urls import path
from .views import NewsAPIView, SingleNewsAPIView

urlpatterns = [
    path('api/news/', NewsAPIView.as_view(), name='news-list'),  # GET and POST for the news list
    path('api/news/<int:pk>/', SingleNewsAPIView.as_view(), name='single-news'),  # GET, PUT, DELETE for a single news item
    path('api/news/delete/', NewsAPIView.as_view(), name='delete-all-news'),  # DELETE to remove all news articles
]
