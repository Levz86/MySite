from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
# Default behaviour - Django creates primary keys for you
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default='Levina Premnand, Be Kind')
    date = models.DateField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('artical-detail', args = (str(self.id)))
    