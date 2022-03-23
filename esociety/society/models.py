from django.db import models

class Society(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    year = models.DateTimeField()

    class Meta():
        db_table = "society"

class Flats(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    flat_no = models.CharField(max_length=50)
    flat_type = models.CharField(max_length=50)
    flat_area = models.CharField(max_length=50)
    flat_price = models.CharField(max_length=50)
    flat_description = models.TextField()
    
    class Meta():
        db_table = "flats"


    
