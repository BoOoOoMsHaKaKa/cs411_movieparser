"""movieparser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user import views as user_views
from comment import views as comment_views
from movie import views as movie_views
from django.contrib.auth import views as auth_views
from comment.views import CommentListView,CommentDetailView,CommentCreateView,CommentUpdateView,CommentDeleteView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/',include('movie.urls')),
    path('comment/',include('comment.urls')),
    path('user/',include('user.urls')),
    path('',include('movie.urls')),#<- home page localhost:8000

    path('register/',user_views.register,name = 'register'),
    path('profile/',user_views.profile,name='profile'),
    path('user_friend/',user_views.user_friend,name='user_friend'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),

    #path('comment/',comment_views.comment_show,name='comment'),
    path('comment/',CommentListView.as_view(),name='comment'),
    path('comment/<int:pk>/',CommentDetailView.as_view(),name='comment_detail'),
    path('comment/create/',CommentCreateView.as_view(),name='comment_create'),
    path('comment/<int:pk>/update',CommentUpdateView.as_view(),name='comment_update'),
    path('comment/<int:pk>/delete',CommentDeleteView.as_view(),name='comment_delete'),
    path('comment/search/',comment_views.comment_search,name='comment_search'),

    path('movies/',movie_views.movie_show,name = 'movies'),
    path('directors/',movie_views.director_show,name = 'directors'),
    path('actors/',movie_views.actor_show,name = 'actors'),



    #path('movies/favorite',movie_views.favorite_movie,name="favorite_movie")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
