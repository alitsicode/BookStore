from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from . models import Customeuser
from django import forms

class customusercreationform(UserCreationForm):
    class Meta:
        model=Customeuser
        fields=UserCreationForm.Meta.fields + ('age','avatar')

class customuserchangeform(UserChangeForm):
    class Meta:
        model=Customeuser
        fields=UserChangeForm.Meta.fields

class profile_form(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        user=kwargs.pop('user')
        super(profile_form,self).__init__(*args, **kwargs)
        if not user.is_superuser:
            self.fields['first_name'].disabled=True
            self.fields['last_name'].disabled=True
            self.fields['is_staff'].disabled=True
            self.fields['date_joined'].disabled=True
            self.fields['is_seller'].disabled=True
        self.fields['is_staff'].help_text=None
    class Meta:
        model= Customeuser
        fields=['username','first_name','last_name','avatar','shop_address','bio','email','date_joined','age','is_staff','is_seller','phone','instagram','telegram','Linkdin','Twitter']