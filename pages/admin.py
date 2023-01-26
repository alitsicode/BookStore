from django.contrib import admin
from .models import book,category,BookMark,Like,IpAddress
# Register your models here.

@admin.register(book)
class BookAdmin(admin.ModelAdmin):
    # add price with discount
    list_display=['Title','Price','price_with_discount','seller','Created','exist','cover_tag']
    ordering=['-Created','exist']
    list_filter=['exist','Category','Created']
    search_fields=['Title','Summary']

@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(BookMark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display=['user','books']
    ordering=['-time_marked']
    list_filter=['user','books']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=['user','books']
    ordering=['-time_liked']
    list_filter=['user','books']

admin.site.register(IpAddress)