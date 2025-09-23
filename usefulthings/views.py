from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from usefulthings.models import Wont
from .paginators import MyPagination
from usefulthings.serializers import WontSerializer
from users.permissions import IsOwner


class WontViewSet(ModelViewSet):
    """ViewSet для работы с привычками"""
    queryset = Wont.objects.all().distinct()
    serializer_class = WontSerializer
    pagination_class = MyPagination


    def perform_create(self, serialazer):
        """метод автоматического сохранения пользователя в поле владельца"""
        wont = serialazer.save()
        wont.owner = self.request.user
        wont.save()

    def get_permissions(self):
        """метод распределения прав доступа"""
        if self.action in ["create", ]:
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ["partial_update", "update", "destroy", "retrieve"]:
            self.permission_classes = (IsOwner,)
        return super().get_permissions()

    def get_queryset(self):
        """ Выводим для пользователя только его привычки"""
        return Wont.objects.filter(owner=self.request.user)

class PublishedWontListView(ListAPIView):
    """Контроллер для списка публичных привычек """
    queryset = Wont.objects.filter(is_published=True)
    serializer_class = WontSerializer
    permission_classes = [AllowAny] #Любой пользователь может видеть публичные привычки

