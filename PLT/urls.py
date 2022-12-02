from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

from PLT import settings

schema_view = get_schema_view(
    openapi.Info(
        title="PLT API",
        default_version='v1',
        description="PLT - бизнес-платформа ТЮН ",
        contact=openapi.Contact(email="pyostr@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    path('api/v1/User/', include('user.urls')),

]
urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    re_path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('main', include('index.urls')),

]

urlpatterns += [path('', admin.site.urls), ]

if settings.DEBUG:
    urlpatterns.insert(0, path('/__debug__/', include('debug_toolbar.urls')))

admin.site.site_header = 'PLT'
admin.site.site_title = 'PLT'
admin.site.index_title = ''
