from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Customeuser
from accounts.forms import customuserchangeform,customusercreationform
# Register your models here.

class customuseradmin(UserAdmin):
    add_form=customusercreationform
    form=customuserchangeform
    model=Customeuser
    fieldsets=UserAdmin.fieldsets+(
        (None,{'fields':('age','is_seller','role','avatar','phone','bio','shop_address','Linkdin','instagram','telegram','Twitter')},),
    )
    add_fieldsets=UserAdmin.add_fieldsets+(
        (None,{'fields':('email','age','is_seller','role','avatar','phone','bio','shop_address','Linkdin','instagram','telegram','Twitter')},),
    )
    
admin.site.register(Customeuser,customuseradmin)
