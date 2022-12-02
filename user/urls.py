from django.urls import path

from user.views import CreateAbstractUserAPIView

urlpatterns = [
    path('Create', CreateAbstractUserAPIView.as_view(), name='Create'),
]