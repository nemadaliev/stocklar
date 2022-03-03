from pydantic import BaseModel

# TODO: Node maritial status
# married
# not_married
# divorced
# widow


class ListRequest(BaseModel):
    text: str

    class Config:
        schema_extra = {
            'example': {
                'text': 'AA'
            }
        }


class ListResult(BaseModel):
   pass