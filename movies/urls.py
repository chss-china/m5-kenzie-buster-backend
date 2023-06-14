from django.urls import path
from .views import MoviesListCreateView,MovieDetailView
urlpatterns = [
    path('movies/', MoviesListCreateView.as_view()),
    path("movies/<int:movie_id>/",MovieDetailView.as_view())
    
]