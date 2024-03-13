from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from memes.models import Meme
from memes.serializers import MemeSerializer


class MemeAPIList(generics.ListCreateAPIView):
    queryset = Meme.objects.order_by('time_update')
    serializer_class = MemeSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class MemeAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Meme.objects.order_by('time_update')
    serializer_class = MemeSerializer


class MemeAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Meme.objects.order_by('time_update')
    serializer_class = MemeSerializer







# class MemeViewSet(ModelViewSet):
#     serializer_class = MemeSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Meme.objects.order_by('time_update')
#
#         return Meme.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)
#     def titles(self, request, pk=None):
#         titles = Meme.objects.get(pk=pk)
#         return Response({'titles': titles.title})
