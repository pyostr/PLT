from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from user.models import AbstractUser


class CreateAbstractUserAPIView(CreateAPIView):
    """
    Создание пользователя
    """
    queryset = AbstractUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )