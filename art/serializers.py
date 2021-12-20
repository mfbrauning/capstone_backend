from rest_framework import serializers
from art.models import Artist, Location, Artwork
       
class FullArtworkSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Artwork
        fields = ['id', 'title', 'year', 'medium', 'image', 'artist', 'location']
        depth = 1
        
class ArtistSerializer(serializers.ModelSerializer):
    artworks = FullArtworkSerializer(many=True, read_only=True)
    
    class Meta:
        model = Artist
        fields = ['id','name', 'nationality', 'dob', 'movement', 'image', 'artworks']
        
class LocationSerializer(serializers.ModelSerializer):
    artworks = FullArtworkSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ['id','name', 'type', 'city', 'country', 'website', 'image', 'artworks']
        
        
class ArtworkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artwork
        fields = ['id', 'title', 'year', 'medium', 'image', 'artist', 'location']
        

