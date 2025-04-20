from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PetMemorial(models.Model):
    SPECIES_CHOICES = [
        ("dog", "Dog"),
        ("cat", "Cat"),
        ("rabbit", "Rabbit"),
        ("hamster", "Hamster"),
        ("guinea_pig", "Guinea Pig"),
        ("ferret", "Ferret"),
        ("bird", "Bird"),
        ("parrot", "Parrot"),
        ("turtle", "Turtle"),
        ("lizard", "Lizard"),
        ("snake", "Snake"),
        ("fish", "Fish"),
        ("horse", "Horse"),
        ("goat", "Goat"),
        ("pig", "Pig"),
        ("chicken", "Chicken"),
        ("duck", "Duck"),
        ("frog", "Frog"),
        ("hedgehog", "Hedgehog"),
        ("other", "Other"),
    ]

    photo = models.ImageField(upload_to='photos', null=True, blank=True)
    pet_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    year_of_birth = models.IntegerField()
    year_of_death = models.IntegerField()
    tribute_quote = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    species = models.CharField(choices=SPECIES_CHOICES, max_length=100)
    breed = models.CharField(max_length=100, blank=True, null=True)
    dominant_traits =models.CharField(max_length=100, blank=True, null=True)
    about_pet = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    owner_display_name = models.CharField(blank=True, null=True, max_length=100)


    def __str__(self):
        return self.pet_name


class PetMemorialGalleryImage(models.Model):
    pet_memorial = models.ForeignKey(PetMemorial, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='gallery', null=True, blank=True)
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Gallery image for {self.pet_memorial.pet_name}"


class CandleMessage(models.Model):
    pet_memorial = models.ForeignKey(PetMemorial, on_delete=models.CASCADE, related_name='candles')
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Candle by {self.name} for {self.pet_memorial.pet_name}"