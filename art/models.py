from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    movement = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
       
class Location(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Artwork(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, related_name='artworks')
    year = models.IntegerField()
    medium = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='artworks')
    
    