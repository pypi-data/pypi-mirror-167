from rest_framework import viewsets

from django_to_galaxy.models.invocation import Invocation
from django_to_galaxy.api.serializers.invocation import InvocationSerializer


class InvocationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows histories to be viewed.
    """

    queryset = Invocation.objects.all()
    serializer_class = InvocationSerializer
