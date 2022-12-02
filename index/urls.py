from django.urls import path
import index.views as view


urlpatterns = [
    path('', view.index),
]
