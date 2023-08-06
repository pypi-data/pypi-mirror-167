from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic import AnyHttpUrl

#change this code bellow where is your class doc
from ..socket_manager import doc
######
from ..views.socket_view import get_asyncapi_html


router= APIRouter(tags= ['Scocket Documentations'])


@router.get('/socket.json')
def get_socket_json():
    return jsonable_encoder(doc.main_data)


@router.get('')
def get_socket_documentation():
    async_url= AnyHttpUrl('/socketdoc/socket.json', scheme= 'http')
    return get_asyncapi_html(asyncapi_url= async_url, title= 'Notification Service')