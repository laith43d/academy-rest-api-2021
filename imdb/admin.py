from django.contrib import admin

from imdb.models import Actor, Title, Place

admin.site.register(Actor)
admin.site.register(Title)
admin.site.register(Place)
