

from django.db import models

class Photo(models.Model):
    # vote =models.CharField(max_length=5000,default="")
    img = models.ImageField(upload_to='static/', default="")