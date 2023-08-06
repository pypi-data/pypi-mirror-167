import pydantic

class CapturError(pydantic.BaseModel):
    request_id: str = pydantic.Field(
        "",
        description='A unique identifier for the request sent which caused the error'
    )
    code: str = pydantic.Field(
        "",
        description='The error code. E.g. 400'
    )
    message: str = pydantic.Field(
        "",
        description='Description of the cause of the error'
    )
