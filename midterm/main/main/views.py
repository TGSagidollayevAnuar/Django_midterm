from rest_framework import viewsets, mixins
from rest_framework.permissions import *
from midterm.main.main.serializers import *
from midterm.main.main.models import *


class BookViewSet(mixins,ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdatemodelMixin,
                  viewsets.ViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_permission(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAdminUser,)
        return [permission() for permission in permission_classes]

class JournalViewSet(Mixins,ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdatemodelMixin,
                  viewsets.ViewSet):
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()

    def get_permission(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAdminUser,)
        return [permission() for permission in permission_classes]
