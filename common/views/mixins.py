from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class ExtendedGenericViewSet(GenericViewSet):
    class Meta:
        pass


class ListViewSet(ExtendedGenericViewSet, mixins.ListModelMixin):
    class Meta:
        pass


class CRUViewSet(ExtendedGenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  ):
    class Meta:
        pass


class CRUDViewSet(CRUViewSet,
                  mixins.DestroyModelMixin,
                  ):
    class Meta:
        pass