from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *

# Register your models here.
class CategoryAdmin(ModelAdmin):
    list_display = ('name','id','icon')

class ArticleAdmin(ModelAdmin):
    list_display = ('title','category','user','date')
    search_fields = ('category__name','title')
    list_filter = ('date','user')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)