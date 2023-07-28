from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

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
        Listando os destinos. Os destinos podem ser filtrados por `name`
        que pode user suado como `?name=<cidade>`
        """
        queryset = self.get_queryset()

        if name := self.request.query_params.get("name"):
            queryset = queryset.filter(name__icontains=name)
            if not queryset.exists():
                return Response(data={"mensagem": "Nenhum destino foi encontrado."}, status=status.HTTP_404_NOT_FOUND)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        Criando um destino.
        """
        return super().post(request, *args, **kwargs)


rud_destination = RetrieveUpdateDestroyDestination.as_view()
lc_destination = ListCreateDesination.as_view()
