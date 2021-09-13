from ninja import Schema
from ninja.orm import create_schema

from imdb.models import Title

TitleAutoOut = create_schema(Title, depth=2)
