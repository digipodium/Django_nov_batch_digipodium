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

# create a model for Website News
# headline
# date
# details
# author
# views -> IntegerField

