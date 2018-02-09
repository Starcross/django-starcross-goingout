from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django import forms
from django.forms.models import fields_for_model

from goingout.models import Venue, Ratings

ratings_fields = fields_for_model(Ratings).keys()

class VenueList(ListView):
    model = Venue

class VenueDetailForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'
        # Assign all ratings widgets as disabled radio select buttons
        widgets = {r: forms.RadioSelect(attrs={'disabled': 'disabled'}) for r in ratings_fields}

class VenueDetail(UpdateView):
    # This is a detail class really but will use read only ratings fields to display
    model = Venue
    form_class = VenueDetailForm
    template_name = 'goingout/venue_detail.html'

    def get_context_data(self, **kwargs):
        context = super(VenueDetail, self).get_context_data(**kwargs)
        # Create a list of fields for the ratings section, to iterate in the template
        context['ratings'] = [context['form'][r] for r in ratings_fields]
        context['venue_list'] = Venue.objects.all() # Provide other venues for display on the map
        context['map_zoom'] = 13 # Use a closer zoom for the detail view
        return context

