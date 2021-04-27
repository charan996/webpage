from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
from datetime import date

class ExtPro(models.Model):
	is_farmer = models.BooleanField(default=False)
	age = models.IntegerField(default=10)
	mobile_number=models.CharField(max_length=12,default="")
	impf=models.ImageField(upload_to='pro/',default="user logo.png")
	address=models.CharField(max_length=100,default="")
	u = models.OneToOneField(User,on_delete=models.CASCADE)


@receiver(post_save,sender=User)
def createpf(sender,instance,created,**kwargs):
	if created:
		ExtPro.objects.create(u=instance)


class Vegpro(models.Model):
	v = [('vegetables',"Vegetables"),('Fruits','Fruits')]
	item_type=models.CharField(max_length=10,choices=v)
	item_name=models.CharField(max_length=20)
	quantity=models.IntegerField(default="")
	is_farmer = models.IntegerField(default=0)
	is_stock = models.IntegerField(default=0)
	price=models.DecimalField(max_digits=6,decimal_places=2)
	impf=models.ImageField(upload_to='images/')
	create_date=models.DateField(auto_now_add=True)
	a=models.ForeignKey(User,on_delete=models.CASCADE)

class UserPro(models.Model):
	farmers_name=models.CharField(max_length=10)
	item_type=models.CharField(max_length=10)
	item_name=models.CharField(max_length=20)
	quantity=models.IntegerField(default="")
	price=models.DecimalField(max_digits=6,decimal_places=2)
	is_status=models.IntegerField(default=0)
	e=models.ForeignKey(Vegpro,on_delete=models.CASCADE)

