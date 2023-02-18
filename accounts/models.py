from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Customeuser(AbstractUser):
    age=models.PositiveIntegerField(null=True,blank=True,default=0)
    is_seller=models.BooleanField(default=False)
    role=models.CharField(_("role"), max_length=50,blank=True,null=True)
    email=models.EmailField(max_length=254,unique=True)
    first_name=models.CharField(max_length=200,default='firstname')
    last_name=models.CharField(max_length=200,default='lastname')
    avatar=models.FileField(null=True,blank=True,upload_to='user_avatar')
    phone=models.CharField(max_length=11,null=True,blank=True)
    telegram=models.CharField(max_length=100,blank=True,null=True)
    instagram=models.CharField(max_length=100,blank=True,null=True)
    Twitter=models.CharField(max_length=100,blank=True,null=True)
    Linkdin=models.CharField(max_length=100,blank=True,null=True)
    bio=models.CharField(max_length=300,default='your bio')
    shop_address=models.CharField(max_length=500,blank=True,null=True)
    class Meta:
        verbose_name=_('CustomeUser')
