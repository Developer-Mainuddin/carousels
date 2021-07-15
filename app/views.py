from django.shortcuts import render

from .models import Carousel, Carouselcircle, Carouselsquare

# Create your views here.

def carouselpage(request):

    carousel = Carousel.objects.all()
    carouselcircle = Carouselcircle.objects.all()
    carouselsquare = Carouselsquare.objects.all()

    context = {
        'carousel':carousel,
        'carouselcircle':carouselcircle,
        'carouselsquare':carouselsquare
    }

    return render(request, 'index.html', context)
