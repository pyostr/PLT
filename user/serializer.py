from rest_framework import serializers

from user.models import AbstractUser


class AbstractUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractUser
        fields = "__all__"
