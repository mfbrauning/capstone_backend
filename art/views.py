from rest_framework.response import Response
from art.models import Artist, Location, Artwork
from art.serializers import ArtistSerializer, LocationSerializer, FullArtworkSerializer, ArtworkSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    
class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
       
class FullArtworkList(generics.ListAPIView):
    queryset = Artwork.objects.all()
    serializer_class = FullArtworkSerializer
    
class FullArtworkDetail(generics.RetrieveAPIView):
    queryset = Artwork.objects.all()
    serializer_class = FullArtworkSerializer
    
class WorkingArtworkList(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    
class WorkingArtworkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer

    

    

 
    