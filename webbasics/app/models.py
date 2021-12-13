from django.db import models

# Create your models here.
class Article(models.Model):
    # title, subject, content, date, is_published
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class News(models.Model):
    headline = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    details =models.TextField()
    author = models.CharField(max_length=30, default="Zaid kamil")
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News List"
    

    def __str__(self) -> str:
        return self.headline


class Contact(models.Model):
    """Model definition for Contact."""

    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10,help_text="mobile number should be of 10 digits")
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name
