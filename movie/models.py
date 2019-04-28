from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class People(models.Model):
    personID = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    birthYear = models.CharField(max_length=255)
    Profession = models.CharField(max_length=255)
    knownforTitles = models.CharField(max_length=255)
    #image = models.ImageField(default='people_pics/default.jpg',upload_to='people_pics')
    #favorite_genre =
    def __str__(self): # how we want it to print out
        return self.name

class Movies(models.Model):
    movieID = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255,null=True)
    releaseYear = models.CharField(max_length=255,null=True)
    runtimeMinutes = models.IntegerField(null=True)
    genres = models.CharField(max_length=255,null=True)
    averageRating=models.FloatField(null=True)
    numVotes = models.IntegerField(null=True)
    introduction = models.TextField(null=True)
    image = models.ImageField(default='movie_pics/default.jpg',upload_to='movie_pics')
    favorite_by = models.ManyToManyField(User,related_name ='favorite_by',blank=True)
    def __str__(self): # how we want it to print out
        return self.title

class Movie_Rating(models.Model):
    movie_ID = models.ForeignKey(Movies, on_delete=models.CASCADE)
    averageRating = models.FloatField()
    numVotes = models.IntegerField()

    def __str__(self): # how we want it to print out
        return self.movie_ID
#people table:

#CREATE TABLE people(personID varchar(255),Name varchar(255),birthYear varchar(255), deathYear varchar(255),Profession varchar(255),knownforTitles varchar(255));

#LOAD DATA INFILE '/Users/Sunny/Desktop/People.tsv' INTO TABLE people FIELDS TERMINATED BY '\t' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;

#movie table:

#CREATE TABLE movies(movieID varchar(255),titleType varchar(255),primaryTitle varchar(255), originalTitle varchar(255),isAdult varchar(255),releaseYear varchar(255),
#endYear varchar(255),length varchar(255), genres varchar(255));

#LOAD DATA INFILE '/Users/Sunny/Desktop/movies.tsv' INTO TABLE movies FIELDS TERMINATED BY '\t' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;

#ALTER TABLE movies DROP COLUMN titleType;
#ALTER TABLE movies DROP COLUMN endYear;


#movie rating table:

#CREATE TABLE movieratings(movieID varchar(255),averageRating varchar(255),numVotes varchar(255));

#LOAD DATA INFILE '/Users/Sunny/Desktop/movieratings.tsv' INTO TABLE movieratings FIELDS TERMINATED BY '\t' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;
