from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="category/")

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100, unique=True, default="Web Article")
    hero_img = models.ImageField(upload_to="articles/")
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING) 
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
