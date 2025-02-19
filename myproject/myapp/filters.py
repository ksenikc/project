import django_filters
from .models import Application


class OrdersFilter(django_filters.FilterSet):
    class Meta:
        model = Application
        fields = {
            'stat',
            'owner',
            'categor',
        }
