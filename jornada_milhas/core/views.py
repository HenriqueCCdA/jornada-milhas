from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from jornada_milhas.core.models import Destination, Post
from jornada_milhas.core.serializer import DestinationSerializer, PostSerializer


class RetrieveUpdateDestroyPost(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, *args, **kwargs):
        """
        Lendo um depoimento pelo `id`.
        """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Atualizando um depoimento pelo `id`.
        """
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        Atualizando um depoimento pelo `id`.
        """
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Deletando um depoimento pelo `id`.
        """
        return super().delete(request, *args, **kwargs)


class ListCreatePost(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, *args, **kwargs):
        """
        Listando as depoimento.
        """
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Criando um depoimento.
        """
        return super().post(request, *args, **kwargs)


class PostHome(APIView):
    def get(self, resquest):
        # TODO: Temo fazer isso de outra forma ?
        posts = Post.objects.order_by("?")[:3]

        serialiazer = PostSerializer(instance=posts, many=True)

        return Response(data={"results": serialiazer.data})


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


rud_post = RetrieveUpdateDestroyPost.as_view()
lc_post = ListCreatePost.as_view()
post_home = PostHome.as_view()


rud_destination = RetrieveUpdateDestroyDestination.as_view()
lc_destination = ListCreateDesination.as_view()
