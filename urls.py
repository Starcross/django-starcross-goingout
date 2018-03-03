from django.urls import path

from goingout.views import VenueList, VenueDetail

app_name = 'goingout'
urlpatterns = [
    # /goingout/venue_list
    path('', VenueList.as_view(), name='venue_list'),
    # /goingout/2/the-red-lion
    path('<int:pk>/<slug>/', VenueDetail.as_view(), name='venue')
]
