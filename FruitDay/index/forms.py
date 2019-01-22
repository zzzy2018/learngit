from django import forms
from .models import *

class LoginForm(forms.ModelForm):
  class Meta:
    #指定关联的Model
    model = User
    #指定要显示的控件
    fields = ["uphone",'upwd']
    #指定每个控件对应的label
    labels = {
      "uphone":'用户名',
      'upwd':'密码',
    }
    #指定每个控件对应的小部件，并给出其他属性
    widgets = {
      'uphone':forms.TextInput(attrs={
        'class':'form-control',
      }),
      'upwd':forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'请输入密码',
      }),
    }






