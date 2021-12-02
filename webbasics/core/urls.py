from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='homepage'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact, name='contact')
]
