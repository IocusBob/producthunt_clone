from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    title =  models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    published_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="icons/")
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pretty_published_date(self):
        return self.published_date.strftime('%b %e %Y')
