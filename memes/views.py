from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from memes.models import Meme
from memes.serializers import MemeSerializer


class MemeViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):

    serializer_class = MemeSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Meme.objects.order_by('time_update')

        return Meme.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def titles(self, request, pk=None):
        titles = Meme.objects.get(pk=pk)
        return Response({'titles': titles.title})
