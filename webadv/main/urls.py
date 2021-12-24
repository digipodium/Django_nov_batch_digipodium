from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', TemplateView.as_view(template_name='about.html'), name="about"),
    path('terms/', TemplateView.as_view(template_name='tnc.html'),name="terms"), 
    path('article/<int:id>/',views.article_detail, name='article'),
]