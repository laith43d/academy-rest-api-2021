from typing import List

from ninja import Router

from imdb.models import Title
from imdb.schemas.titles_schemas import TitleAutoOut

titles_controller = Router(tags=['title'])


@titles_controller.get('/list', response={200: List[TitleAutoOut]})
def list_titles(request):
    return Title.objects.all()
