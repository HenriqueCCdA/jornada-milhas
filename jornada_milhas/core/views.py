from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from jornada_milhas.core.models import Post
from jornada_milhas.core.serialiazer import PostSerialiazer


class RetrieveUpdateDestroyPost(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazer

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
    serializer_class = PostSerialiazer

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


rud_post = RetrieveUpdateDestroyPost.as_view()
lc_post = ListCreatePost.as_view()
