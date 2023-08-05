import django_filters
from django.db.models import Q

from nautobot.extras.filters import NautobotFilterSet
from nautobot.utilities.choices import ColorChoices
from nautobot.utilities.filters import BaseFilterSet
from nautobot.tenancy.models import Tenant

from .models import CableTemplate, CablePlug


class CableTemplateFilterSet(NautobotFilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )

    owner_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        label="Owner (ID)",
        required=False,

    )
    owner = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        field_name="owner__slug",
        to_field_name="slug",
        label="Owner (Slug)",
        required=False,

    )

    plug_id = django_filters.ModelMultipleChoiceFilter(
        queryset=CablePlug.objects.all(),
        label="Plug (ID)",
        required=False,
    )
    plug = django_filters.ModelMultipleChoiceFilter(
        queryset=CablePlug.objects.all(),
        field_name="plug__name",
        to_field_name="name",
        label="Plug (Name)",
        required=False,
    )

    class Meta:
        model = CableTemplate
        fields = ['cable_number', 'type', 'color']

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
                Q(cable_number__icontains=value) |
                Q(label__icontains=value)
        )
        return queryset.filter(qs_filter)
