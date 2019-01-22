from django.contrib import admin
from .models import *

class GoodsAdmin(admin.ModelAdmin):
  #指定在列表页中显示的字段们
  list_display = ('title','goodsType','price','spec')
  #指定右侧显示的过滤器
  list_filter = ('goodsType',)
  #指定在上方显示的搜索字段们
  search_fields = ('title',)

# Register your models here.
admin.site.register(GoodsType)
admin.site.register(Goods,GoodsAdmin)