from django.db import models
from django.forms import RadioSelect
from geoposition.fields import GeopositionField
from tinymce.models import HTMLField

# Venue models definitions

scores = [(i,i) for i in range(11)]


class Ratings(models.Model):
    """ Abstract class for venue ratings """

    food = models.IntegerField(choices=scores,default=0)
    beer = models.IntegerField(choices=scores,default=0)
    wine = models.IntegerField(choices=scores,default=0)
    service = models.IntegerField(choices=scores,default=0)
    value = models.IntegerField(choices=scores,default=0)

    class Meta:
        abstract = True


class Venue(Ratings):

    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    review = HTMLField(blank=True)
    website = models.URLField(blank=True)
    position = GeopositionField()

    def __str__(self):
        return self.title





