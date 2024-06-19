from django.db import models
from django.core.files.storage import FileSystemStorage


fileSystem = FileSystemStorage(location='pages/static')



class Vendor(models.Model):
    companyName = models.CharField(max_length=255)
    established = models.DateField()
    employeesCount = models.IntegerField()
    internalProfessionalService = models.BooleanField()
    lastDemo = models.DateField()
    lastReview = models.DateField()
    companyDisplayPicture = models.ImageField(storage=fileSystem,upload_to='company_display_pics/')
    companyBackgroundPicture = models.ImageField(storage=fileSystem,upload_to='company_background_pics/')
    company_url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.companyName

class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='products')
    productName = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(storage=fileSystem, upload_to='product_images/')
    business_area = models.CharField(max_length=255)
    modules = models.CharField(max_length=255)
    financialServicesClientTypes = models.CharField(max_length=255)
    cloud = models.BooleanField()

    def __str__(self):
        return self.productName
