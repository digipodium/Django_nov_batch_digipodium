from django.contrib import admin
from app.models import *
# Register your models here.

admin.site.register(Article)
admin.site.register(News)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for Contact'''

    list_display = ('name','email','mobile','message','date')
    list_filter = ('date',)