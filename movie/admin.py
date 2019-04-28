from django.contrib import admin
from .models import People,Movies,Movie_Rating
# Register your models here.
admin.site.register(People)
admin.site.register(Movies)
admin.site.register(Movie_Rating)
