from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django import forms
from django.forms import fields_for_model, modelformset_factory

from goingout.models import Venue, Ratings

ratings_fields = fields_for_model(Ratings).keys()


class VenueDetailForm(forms.ModelForm):
    ratings = None

    class Meta:
        model = Venue
        fields = '__all__'
        # Assign all ratings widgets as disabled radio select buttons
        widgets = {r: forms.RadioSelect(attrs={'disabled': 'disabled'}) for r in ratings_fields}


class VenueDetail(UpdateView):
    """ This is a effectively a detail class but will use read-only ratings form fields to display """
    model = Venue
    form_class = VenueDetailForm
    template_name = 'goingout/venue_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Create a list of fields for the ratings section, to iterate in the template
        context['ratings'] = [context['form'][r] for r in ratings_fields]
        context['venue_list'] = Venue.objects.all()  # Provide other venues for display on the map
        context['map_zoom'] = 13  # Use a closer zoom for the detail view
        return context


class VenueList(ListView):
    """ The front page view of large map and latest reviews. Venues also accessed via a form
    as ratings need radio controls """
    model = Venue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        formset = modelformset_factory(Venue, form=VenueDetailForm, extra=0)
        context['form'] = formset()
        for i, venue in enumerate(context['form']):
            context['form'][i].ratings = [context['form'][i][r] for r in ratings_fields]
            # Make the slug available in the form as well. Assumes form items and object_list
            # are in the same order
            context['form'][i].slug = self.object_list[i].slug
        return context
