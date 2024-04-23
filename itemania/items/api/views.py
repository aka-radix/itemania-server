from rest_framework import viewsets
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from itemania.items.models import Item

from .serializers import BaseItemSerializer, ItemSerializer


class ItemViewSet(
    viewsets.GenericViewSet,
    ListModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return BaseItemSerializer

        return self.serializer_class
