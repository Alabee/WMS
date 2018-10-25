from django.db import models

# Create your models here.
class Firm(models.Model):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=20)#to be fixed later
    motto = models.CharField(max_length=50)
    phone_number_manager = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Writer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number_writer = models.CharField(max_length=50)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name