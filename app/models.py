from django.db import models

# Create your models here.


class Carousel(models.Model):

    heading = models.CharField(max_length=100)
    paragraph = models.TextField()
    background = models.ImageField()

class Carouselcircle(models.Model):

    heading1 = models.CharField(max_length=100)
    paragraph1 = models.TextField()
    background1 = models.ImageField()

class Carouselsquare(models.Model):

    heading2 = models.CharField(max_length=100)
    paragraph2 = models.TextField()
    background2 = models.ImageField()
    
