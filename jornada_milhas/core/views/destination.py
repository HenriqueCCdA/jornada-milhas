from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser

from jornada_milhas.core.models import Destination
from jornada_milhas.core.serializer import DestinationSerializer


class RetrieveUpdateDestroyDestination(RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, *args, **kwargs):
        """
        Lendo um destino pelo `id`.
        """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Atualizando um destino pelo `id`.
        """
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        Atualizando um destino pelo `id`.
        """
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Deletando um destino pelo `id`.
        """
        return super().delete(request, *args, **kwargs)


class ListCreateDesination(ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, *args, **kwargs):
        """
        Listando os destinos.
        """
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Criando um destino.
        """
        return super().post(request, *args, **kwargs)


rud_destination = RetrieveUpdateDestroyDestination.as_view()
lc_destination = ListCreateDesination.as_view()
