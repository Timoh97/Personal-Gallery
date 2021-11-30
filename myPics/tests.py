from django.test import TestCase
from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.mombasa= Location(description = 'beautiful place', name ='Mombasa')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.mombasa,Location))
        
        
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.philosophy= Category(name = 'Philosophy')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.philosophy,Category))
        
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.mahatma = Image(image ='pic',name = 'Mahatma', description='beautiful place',location='Paris',category='philosophy')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.mahatma,Image))
        
        # Testing Save Method
    def test_save_method(self):
        self.mahatma.save_images()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)
    
    def test_update_method(self):
        self.mahatma.update_images()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)
