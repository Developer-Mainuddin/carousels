from django.urls import include, path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.carouselpage, name='carouselpage')
]
