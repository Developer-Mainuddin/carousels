from django.contrib import admin

from .models import Carousel, Carouselcircle, Carouselsquare

# Register your models here.


class CarouselAdmin(admin.ModelAdmin):

    list_display = [
        'heading',
        'paragraph',
        'background'
    ]

admin.site.register(Carousel, CarouselAdmin)

class CarouselcircleAdmin(admin.ModelAdmin):

    list_display = [
        'heading1',
        'paragraph1',
        'background1'
    ]

admin.site.register(Carouselcircle, CarouselcircleAdmin)

class CarouselsquareAdmin(admin.ModelAdmin):

    list_display = [
        'heading2',
        'paragraph2',
        'background2'
    ]

admin.site.register(Carouselsquare, CarouselsquareAdmin)
