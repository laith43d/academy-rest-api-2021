from datetime import date
from typing import List
from ninja import Schema
from ninja.orm import create_schema

from imdb.models import Actor, Place


class PlaceOut(Schema):
    id: int
    name: str
    location: float


class ActorSchema(Schema):
    name: str = None
    bio: str = None
    date_of_birth: date = None


class ActorOut(ActorSchema):
    id: int
    place_of_birth: PlaceOut


class ActorIn(ActorSchema):
    place_of_birth: int = None

#
# PlaceAutoOut = create_schema(Place, exclude=['location'])
#
# ActorAutoOut = create_schema(Actor, depth=1, exclude=['photo'], custom_fields=[
#     ('place_of_birth', PlaceAutoOut, None)
# ])
