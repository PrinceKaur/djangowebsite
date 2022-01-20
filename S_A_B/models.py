from django.db import models

# Create your models here.
class shop(models.Model):
	shop_id=models.AutoField
	shop_name=models.CharField(max_length=50)
	desc=models.CharField(max_length=500)
	date=models.DateField()
# cart
class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)