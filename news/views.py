from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import News
from .serializers import NewsSerializer

class NewsAPIView(APIView):
    # GET method - List all news
    def get(self, request):
        news = News.objects.all()  # Get all news articles from the database
        serializer = NewsSerializer(news, many=True)  # Serialize them
        return Response(serializer.data)  # Return serialized data in the response

    # POST method - Create a new news article
    def post(self, request):
        serializer = NewsSerializer(data=request.data)  # Get data from the request body
        if serializer.is_valid():  # Check if the data is valid
            serializer.save()  # Save the new news article to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return success response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return error if invalid data

    # DELETE method - Delete all news articles
    def delete(self, request):
        News.objects.all().delete()  # Delete all news articles in the database
        return Response({"detail": "All news articles have been deleted."}, status=status.HTTP_204_NO_CONTENT)


class SingleNewsAPIView(APIView):
    # GET method - Retrieve a specific news article by ID
    def get(self, request, pk):
        try:
            news_item = News.objects.get(pk=pk)  # Get the specific news item by its ID
        except News.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = NewsSerializer(news_item)  # Serialize the news item
        return Response(serializer.data)  # Return the serialized data

    # PUT method - Update an existing news article
    def put(self, request, pk):
        try:
            news_item = News.objects.get(pk=pk)  # Get the specific news item by ID
        except News.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = NewsSerializer(news_item, data=request.data)  # Deserialize and validate the incoming data
        if serializer.is_valid():
            serializer.save()  # Save the updated news article
            return Response(serializer.data)  # Return the updated data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method - Delete a specific news article by ID
    def delete(self, request, pk):
        try:
            news_item = News.objects.get(pk=pk)  # Get the specific news item by ID
        except News.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        news_item.delete()  # Delete the news article
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return a no content status
