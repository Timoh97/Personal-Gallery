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
        self.mahatma= Image(name = 'Mahatma', description='beautiful place',location='Mahatma',category='philosophy')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.mahatma,Image))
