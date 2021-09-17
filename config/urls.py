from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from imdb.controllers.actors_controller import actors_controller
from imdb.controllers.titles_controller import titles_controller
# from rest_auth._controllers import test_api
from rest_auth.controllers.auth import auth

api = NinjaAPI(
    version='1.0.0',
    title='client API v1',
    description='API documentation',
)

# api.add_router('/test', test_api)
api.add_router('/actor', actors_controller)
api.add_router('/title', titles_controller)
api.add_router('/auth', auth)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
