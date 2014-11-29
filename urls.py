from django.conf.urls import patterns, url

from views import VenueList, VenueDetail

urlpatterns = patterns('',
    # ex: /goingout/
    url(r'^$', VenueList.as_view(), name='venue_list'),
    url(r'^(?P<pk>\d+)/$', VenueDetail.as_view(), name='venue'),

)