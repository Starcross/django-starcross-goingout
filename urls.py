from django.urls import path

from goingout.views import VenueList, VenueDetail

app_name = 'goingout'
urlpatterns = [
    # ex: /goingout/
    path('', VenueList.as_view(), name='venue_list'),
    path('<int:pk>', VenueDetail.as_view(), name='venue')
]
