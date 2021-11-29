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
     
     
    def save_images(self):
        self.save()
        
    def update_images(self,description,category,location):
        self.description = description
        self.location = location
        self.category = category
        self.save()
        
           
    @classmethod
    def search_image(cls,search_term):
        image = cls.objects.filter(name__icontains=search_term)
        return image
    
    @classmethod
    def filter_by_location(cls, location):
        images = Image.objects.filter(location_name=location)
        return images
    
    @classmethod
    def search_image_location(cls,search_term):
        image_location = cls.objects.filter_by_location(location_icontains=search_term)
        return image_location
    
    
    
    
