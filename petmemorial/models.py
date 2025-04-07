from django.db import models

# Create your models here.
class Person(models.Model):
    image = models.ImageField(upload_to='test-uploads/')

    def __str__(self):
        return f"Person {self.id}"
