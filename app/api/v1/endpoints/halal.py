import json
from typing import Any
from urllib import request, response
from urllib.request import urlopen

from fastapi import APIRouter, Depends, Request
from pydantic.networks import EmailStr

from app import schemas
from app.core.config import settings
from app.services.utils import DataService

router = APIRouter()


@router.post("/check")
def check(req: schemas.halal.HalalRequest) -> Any:
    income_statement = DataService.incomeStatement('Salom')

    return income_statement

# def check(req: schemas.halal.HalalRequest) -> Any:
#     respond = urlopen("{}/income-statement/{}?apikey={}".format(settings.API_ENDPOINT, req.symbol, settings.API_KEY ))
#     data_json = json.loads(respond.read())
#
#     return data_json
