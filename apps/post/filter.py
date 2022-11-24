


from django.forms import IntegerField
from django_filters import rest_framework as filters
from .models import Apartment

class ApartmentFilter(filters.FilterSet):
    # square_meters = IntegerField()
    rooms = filters.RangeFilter()

    class Meta:
        model = Apartment
        fields = ['rooms']