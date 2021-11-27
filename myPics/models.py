from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =300)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length =30)
    
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =300)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
    
