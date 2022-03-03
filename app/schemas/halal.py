from pydantic import BaseModel

# TODO: Node maritial status
# married
# not_married
# divorced
# widow


class HalalRequest(BaseModel):
    symbol: str

    class Config:
        schema_extra = {
            'example': {
                'symbol': 'TSLA'
            }
        }


class HalalResult(BaseModel):
   pass