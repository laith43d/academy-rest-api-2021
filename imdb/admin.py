from django.contrib import admin

from imdb.models import Actor, Title, Place, Genre

admin.site.register(Actor)
admin.site.register(Title)
admin.site.register(Place)
admin.site.register(Genre)
