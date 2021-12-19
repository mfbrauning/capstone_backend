from django.urls import path
from art import views

urlpatterns = [
    path('artists/', views.ArtistList.as_view()),
    path('artists/<int:pk>/', views.ArtistDetail.as_view()),
    path('locations/', views.LocationList.as_view()),
    path('locations/<int:pk>/', views.LocationDetail.as_view()),
    path('artworks/', views.FullArtworkList.as_view()),
    path('artworks/<int:pk>/', views.FullArtworkDetail.as_view()),
    path('artworksedit/', views.WorkingArtworkList.as_view()),
    path('artworksedit/<int:pk>/', views.WorkingArtworkDetail.as_view())
]