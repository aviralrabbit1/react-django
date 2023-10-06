from django.db import models

# Create your models here.
class firstapp(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return f"Name: {self.title}"
