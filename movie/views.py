from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages,auth
from .models import Movies,People,Movie_Rating
from django.db import connection
from django.contrib.auth.models import User
import operator
import json
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    user = auth.get_user(request)
    #favorite_movies=Movies('favorite_by.')
    favorite_movies_id=[]
    for i in Movies.objects.all():
        for j in i.favorite_by.all():
            if j.id ==user.id :
                favorite_movies_id.append(i.movieID)
    print(favorite_movies_id)
    genre_dict={}
    for i in Movies.objects.all():
        if i.movieID in favorite_movies_id :
            print(i.genres)
            genres =i.genres
            idx=0
            temp=""
            while(idx<len(genres)):
                if genres[idx]!=',':
                    temp+=genres[idx]
                if temp =='Animation' or temp =='Comedy'or temp =='Romance' or temp =='Horror' or temp =='Drama' or temp =='Sci-Fi' or temp =='Biography' or temp =='Adventure' or temp =='Action' or temp =='Music' :
                    if temp not in genre_dict:
                        genre_dict[temp] =1
                        temp=''
                    else:
                        genre_dict[temp] =genre_dict[temp] +1
                        temp=''
                idx =idx+1
    print("genre:")
    print(genre_dict)
    if genre_dict!={}:
        max_genre_1 = max(genre_dict, key=genre_dict.get)
        del genre_dict[max_genre_1]
        max_genre_2 = max(genre_dict, key=genre_dict.get)
        del genre_dict[max_genre_2]
        max_genre_3 = max(genre_dict, key=genre_dict.get)
        print(max_genre_1)
        print(max_genre_2)
        print(max_genre_3)
        recommend_movies_dict={}
        recommend_movies=[]
        curr_lowest_rate = 10
        movie_score={}
        for i in Movies.objects.all():
            movie_score[i]=0
            #50000 vote increase by 0.1
            if i.genres.find(max_genre_1):
                movie_score[i] = movie_score[i]+10
            if i.genres.find(max_genre_2):
                movie_score[i] = movie_score[i]+7
            if i.genres.find(max_genre_3):
                movie_score[i] = movie_score[i]+5
            movie_score[i] = movie_score[i]+i.averageRating*(i.numVotes)/1000000.0 -(2019-int(i.releaseYear)/20.0)
        max_movie_score_1 = max(movie_score, key=movie_score.get)
        del movie_score[max_movie_score_1]
        max_movie_score_2 = max(movie_score, key=movie_score.get)
        del movie_score[max_movie_score_2]
        max_movie_score_3 = max(movie_score, key=movie_score.get)
        del movie_score[max_movie_score_3]
        recommend_movies = [max_movie_score_1,max_movie_score_2,max_movie_score_3]
        print("recomment movie")
        print(recommend_movies)
    else:
        recommend_movies={}
    ################# recommend Friends
    print("current_user???")

    curr_user = auth.get_user(request)
    print(curr_user)
    favorite_movies_id={}
    for user in User.objects.all():
        favorite_movies_id[user]=[]
        for i in Movies.objects.all():
            for j in i.favorite_by.all():
                if j.id ==user.id :
                    favorite_movies_id[user].append(i.movieID)
    print(favorite_movies_id) #-> all users' preference movie_id dictionary{user_ID: [movie_id,movie_id,..]}

    score_dict={}
    # calculate the overlap of movies
    for user in favorite_movies_id.keys():
        if curr_user!=user:
            #len(set(a).intersection(set(b)))
            print(favorite_movies_id[curr_user])
            print(favorite_movies_id[user])
            print(set(favorite_movies_id[curr_user]).intersection(set(favorite_movies_id[user])))
            score_dict[user]=10*len(set(favorite_movies_id[curr_user]).intersection(set(favorite_movies_id[user])))
    print(score_dict)
    #calculate the overlap of genres max_genre_1,max_genre_2,max_genre_3
    if genre_dict!={}:
        for user in favorite_movies_id.keys():
            if curr_user!=user:
                genre_dict={}
                for i in Movies.objects.all():
                    if i.movieID in favorite_movies_id[user] :
                        print(i.genres)
                        genres =i.genres
                        idx=0
                        temp=""
                        while(idx<len(genres)):
                            if genres[idx]!=',':
                                temp+=genres[idx]
                            if temp =='Animation' or temp =='Comedy'or temp =='Romance' or temp =='Horror' or temp =='Drama' or temp =='Sci-Fi' or temp =='Biography' or temp =='Adventure' or temp =='Action' or temp =='Music' :
                                if temp not in genre_dict:
                                    genre_dict[temp] =1
                                    temp=''
                                else:
                                    genre_dict[temp] =genre_dict[temp] +1
                                    temp=''
                            idx =idx+1
                print("other user genre dict :")
                print(genre_dict)
                #1->6*num_of_genre ,2->4*num_of_genre,3->2*num_of_genre
                if max_genre_1 in genre_dict.keys():
                    score_dict[user] =score_dict[user] + 6*genre_dict[max_genre_1]
                if max_genre_2 in genre_dict.keys():
                    score_dict[user] =score_dict[user] + 4*genre_dict[max_genre_2]
                if max_genre_3 in genre_dict.keys():
                    score_dict[user] =score_dict[user] + 2*genre_dict[max_genre_3]
        print("final_result")
        print(score_dict)
        friend_1 = max(score_dict, key=score_dict.get)
        del score_dict[friend_1]
        friend_2 = max(score_dict, key=score_dict.get)
        del score_dict[friend_2]
        friend_3 = max(score_dict, key=score_dict.get)
        del score_dict[friend_3]

        recommend_friends=[friend_1,friend_2,friend_3]
        print(recommend_friends)
    else:
        recommend_friends=[]



    context={'movies':recommend_movies,'friends':recommend_friends}
    return render(request,'movie/home_page.html',context)#request,template_name

def movie_show(request):
    # display all the movies on the page
    movies = Movies.objects.all().order_by('-releaseYear')
    context = {'movies':movies}
    #movie = get_object_or_404(Movies,movieID = request.POST.get('movie.movieID'))
    ##movie.favorite_by.add(request.user)
    # check for favorite
    #user = auth.get_user(request)
    return render(request,'movie/movies.html',context)#request,template_name

#def favorite_movie(request):
    #movie = get_object_or_404(Movies,id = request.POST.get('movie.movieID'))
    ##print(movie.title)
    #movie.favorite_by.add(request.user)
    #return render(request,'movie/movies_html')

def director_show(request):
    directors=[]
    for person in People.objects.all():
        if 'director' in person.Profession :
            directors.append(person)
    context={'directors':directors}
    print(directors)
    return render(request,'movie/directors.html',context)

def actor_show(request):
    actors=[]
    for person in People.objects.all():
        if 'actor' in person.Profession or  'actress' in person.Profession:
            actors.append(person)
    context={'actors':actors}

    return render(request,'movie/actors.html',context)
