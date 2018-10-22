from django.db import models
from firm.models import Writer

# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=20)
    discipline = models.CharField(max_length=20)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    deadline_client = models.CharField(max_length=20)
    deadline_writer = models.CharField(max_length=20)
    compensation_client = models.CharField(max_length=20)
    compensation_writer = models.CharField(max_length=20)
    instruction = models.CharField(max_length=20)
    attachment = models.CharField(max_length=20)
    

    def __str__(self):
        return self.name
