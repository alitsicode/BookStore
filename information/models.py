from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import Customeuser
# Create your models here.

class About_Us(models.Model):
    shop_name=models.CharField(_("Shop_name"), max_length=50)
    description=models.TextField(_("description"))
    phone=models.CharField(verbose_name=_('Phone number'), max_length=10,default='9015738669')
    telegram=models.CharField(_("telegram"), max_length=70,blank=True)
    instagram=models.CharField(_("instagram"), max_length=70,blank=True)
    linkdin=models.CharField(_("Linkdin"), max_length=70,blank=True)
    whatsapp=models.CharField(_("whatsapp"), max_length=70,blank=True)
    reward=models.TextField(_("reward"),null=True,blank=True)
    inventors=models.ManyToManyField(Customeuser, verbose_name=_("inventors"))
    work_image=models.ImageField(_("Images"), upload_to='work_image')
    def __str__(self):
        return self.shop_name
    def work_image_tag(self):
        return format_html('<img width=150px height=150px src="{}" />'. format(self.work_image.url))
    class Meta:
        verbose_name=_('About u')

class Contact_Us(models.Model):
    user=models.ForeignKey(Customeuser, verbose_name=_("User"), on_delete=models.CASCADE)
    text=models.TextField(_("your text"))
    created=models.DateTimeField(_("created"),auto_now_add=True)
    def __str__(self):
        return self.user
    