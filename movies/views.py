from django.shortcuts import render

from rest_framework.views import APIView, Request, Response, status
from .models import Movie
from rest_framework import permissions
from movies.serializers import MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
    BasePermission,
)
from users.permissions import IsEmployeeOrReadOnly

class MoviesListCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

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