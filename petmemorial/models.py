from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Memorial(models.Model):

    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    owner_name = models.ForeignKey(User,on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=200)
    pet_profile_photo=models.ImageField(upload_to='pet_photos/')
    pet_species = models.CharField(max_length=50)
    pet_breed = models.CharField(max_length=50)
    pet_sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birth_date = models.DateField()
    death_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)
    about_text = models.TextField()
    about_vet_text = models.TextField()


     # Will add Comments and Tags models later
    # comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.pet_name
    





