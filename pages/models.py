from django.db import models
from accounts.models import Customeuser
from django.utils.html import format_html
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


class IpAddress(models.Model):
    ip_address=models.GenericIPAddressField(verbose_name=_('ip_address'))
# Create your models here.
class category(models.Model):
    title=models.CharField(max_length=50,verbose_name=_('category'))
    cover=models.ImageField(_("cover"), upload_to='category_cover',blank=True)
    def __str__(self):
        return self.title

class book(models.Model):
    exist=(
        ('have','have'),
        ('in_order','in_order'),
        ('finish','finish'),
    )
    Title=models.CharField(_("Title"), max_length=50)
    Summary=RichTextField()
    Price=models.BigIntegerField(_("Price"))
    price_with_discount=models.BigIntegerField(_("discount price"),null=True,blank=True)
    Author=models.CharField(_("Author"), max_length=50)
    page_count=models.BigIntegerField(_("Page Count"))
    cover=models.ImageField(_("Cover"), upload_to='cover/')
    hits=models.ManyToManyField(IpAddress,blank=True,through='hitsfilter',related_name='hits',verbose_name=_('views'))
    Category=models.ManyToManyField(category, verbose_name=_("Category"),related_name='books')
    seller=models.ForeignKey(Customeuser, verbose_name=_("seller"), on_delete=models.CASCADE,related_name='books')
    Information=models.TextField(_("Information"),null=True,blank=True)
    Created=models.DateTimeField(_("Created"),auto_now_add=True)
    Updated=models.DateTimeField(_("Edited"), auto_now=True)
    exist=models.CharField(max_length=8,choices=exist,default='have',verbose_name=_('exist'))
    comments = GenericRelation(Comment)
    def cover_tag(self):
        return format_html('<img width=150px height=150px src="{}" />'. format(self.cover.url))
    def __str__(self):
        return self.Title

class BookMark(models.Model):
    user=models.ForeignKey(Customeuser, verbose_name=_("user"),on_delete=models.CASCADE,related_name='bookmark')
    books=models.ForeignKey(book, verbose_name=_("book"), on_delete=models.CASCADE,related_name='bookmark')
    time_marked=models.DateTimeField(_("saved time"), auto_now_add=True)
    def __str__(self):
        return self.user.username

class Like(models.Model):
    user=models.ForeignKey(Customeuser, verbose_name=_("user"),on_delete=models.CASCADE,related_name='like')
    books=models.ForeignKey(book, verbose_name=_("book"), on_delete=models.CASCADE,related_name='like')
    time_liked=models.DateTimeField(_("like time"), auto_now_add=True)
    def __str__(self):
        return {self.user}
    
class hitsfilter(models.Model):
    product=models.ForeignKey(book, verbose_name=_("book"), on_delete=models.CASCADE)
    ip_address=models.ForeignKey(IpAddress, verbose_name=_("ip_address"), on_delete=models.CASCADE)
    timecreated=models.DateTimeField(auto_now_add=True,verbose_name=_('timeview'))

# class Multicoverbook(models.Model):
#     coverbook=models.ImageField(_("cover"), upload_to='cover/')
#     connectbook=models.ForeignKey(book, verbose_name=_("book"), on_delete=models.CASCADE)
#     created=models.DateTimeField(_("time create"),auto_now_add=True)
#     def __str__(self):
#         return self.connectbook
    
