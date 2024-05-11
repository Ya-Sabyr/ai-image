from django.db import models

class Value(models.Model):
    image = models.ImageField('Image', upload_to='images/')
