from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='profile_image/Default.jpg',upload_to='profile_image')# folder that the picture uploads to
    #Friend_list =
    favorite_movies = models.CharField(max_length=255,null=True)
    favorite_actors = models.CharField(max_length=255,null=True)
    favorite_directors = models.CharField(max_length=255,null=True)
    def __str__(self): # how we want it to print out
        return f'{self.user.username } Profile'

    #def save(self):
        #super().save() # upload large Images

        #img = image.open(self.image.path)

        #if img.height >200 or img.width >200:
            #final_size = (200,200)
            #img.thumbnail(final_size)
            #img.save(self.image.path)
