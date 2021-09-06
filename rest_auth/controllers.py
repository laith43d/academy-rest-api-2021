from ninja import Router
from ninja import Schema

test_api = Router(tags=['API Test values'])


class EchoIn(Schema):
    echo_id: int
    echo_name: str


@test_api.get('/echo')
def list_all_echos(request):
    return {'result': 2 + 5}


@test_api.post('/echo/{echo_id}')
def list_one_echos(request, echo_id: int, payload: EchoIn, echo_name: str):
    return payload.dict()


@test_api.post('/echo')
def create_echo(request):
    return {}
