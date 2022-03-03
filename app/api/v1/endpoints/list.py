import json
from typing import Any
from urllib import request, response
from urllib.request import urlopen

from fastapi import APIRouter, Depends, Request, Body
from pydantic.networks import EmailStr

from app import schemas

router = APIRouter()


@router.post("/search")
async def search(request: schemas.list.ListRequest, t: Request) -> Any:
    requestData = await t.json()
    respond = urlopen("https://ticker-2e1ica8b9.now.sh/keyword/{}".format(requestData['text']))
    data_json = json.loads(respond.read())
    return data_json

@router.get("/info")
async  def info(t: Request)->Any:
    requestData = await t.json()
    return {'result': 'Company Json data -> {}'.format(requestData['text'])}