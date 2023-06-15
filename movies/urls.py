from django.urls import path
from .views import MoviesListCreateView,MovieDetailView,MovieOrderView
urlpatterns = [
    path('movies/', MoviesListCreateView.as_view()),
    path("movies/<int:movie_id>/",MovieDetailView.as_view()),
    path("movies/<int:movie_id>/orders/",MovieOrderView.as_view()),
    
]