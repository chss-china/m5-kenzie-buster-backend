from django.shortcuts import render

from rest_framework.views import APIView, Request, Response, status
from .models import Movie
from movies.serializers import MovieSerializer,MovieOrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsEmployeeOrReadOnly,IsUserAuthenticated
from rest_framework.pagination import PageNumberPagination
class MoviesListCreateView(APIView,PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def get(self, request):
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies,request)
        serializer = MovieSerializer(instance=result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]
 
    def get(self, request, movie_id):
        try:
           movie = Movie.objects.get(id=movie_id)
           serializer = MovieSerializer(movie)
           return Response(serializer.data)
        except Movie.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, movie_id):
      try:
          movie = Movie.objects.get(id=movie_id)
          movie.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
      except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
      
class MovieOrderView(APIView):
   authentication_classes = [JWTAuthentication]
   permission_classes = [IsUserAuthenticated]

   def post(self, request,movie_id):
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, movie_id=movie_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    