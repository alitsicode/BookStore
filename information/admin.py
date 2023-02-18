from django.contrib import admin
from .models import About_Us,Contact_Us
# Register your models here.

@admin.register(About_Us)
class AboutusAdmin(admin.ModelAdmin):
    list_display=['shop_name','work_image_tag','address','phone','email']

@admin.register(Contact_Us)
class ContactusAdmin(admin.ModelAdmin):
    list_display=['user','text']
    list_filter=['user']
    ordering=['-created']
