from django.contrib import admin
from django.urls import path, include  # include function is used to include app-specific urls

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('', include('news.urls')),  # Include the URLs from the 'news' app
]
