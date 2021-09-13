from ninja import Router
from typing import List
from imdb.models import Actor
from imdb.schemas.actors_schemas import ActorIn, ActorOut
from django.shortcuts import get_object_or_404

actors_controller = Router(tags=['actor'])


# @actors_controller.get('/list', response=List[ActorAutoOut])
# def list_actors(request):
#     return Actor.objects.all()


@actors_controller.post("/create", response={201: ActorOut})
def create_actor(request, payload: ActorIn):
    pob = payload.place_of_birth
    del payload.place_of_birth
    actor = Actor.objects.create(**payload.dict(), place_of_birth_id=pob)
    return 201, {"id": actor.id}


@actors_controller.get("/retrieve/{actor_id}", response={200: ActorOut})
def retrieve_actor(request, actor_id: int):
    return get_object_or_404(Actor, id=actor_id)


@actors_controller.get("/list", response=List[ActorOut])
def list_actors(request):
    # qs = Actor.objects.filter(place_of_birth__name='Layth').prefetch_related('place_of_birth')
    return Actor.objects.all()


@actors_controller.put("/update/{actor_id}")
def update_actor(request, actor_id: int, payload: ActorIn):
    pob = payload.place_of_birth
    del payload.place_of_birth
    actor = get_object_or_404(Actor, id=actor_id)
    for attr, value in payload.dict().items():
        setattr(actor, attr, value)

    actor.place_of_birth_id = pob
    actor.save()
    return 200, {"success": True}


@actors_controller.delete("/delete/{actor_id}")
def delete_actor(request, actor_id: int):
    actor = get_object_or_404(Actor, id=actor_id)
    actor.delete()
    return 204, {"success": True}
