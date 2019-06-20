from pydantic import BaseModel, validator
from typing import Any, Callable, List

__name__ = 'pydantic'


class SubS(BaseModel):
    class Config:
        orm_mode = True

    w: int
    x: int
    y: str
    z: int

    @validator('x')
    def get_x_val(cls, val):
        return val + 10


class ComplexS(BaseModel):
    class Config:
        orm_mode = True

    foo: str
    bar: Callable[[], int]
    sub: SubS
    subs: List[SubS]

    @validator('bar')
    def get_bar_val(cls, val):
        return val()


def serialization_func(obj, many):
    if many:
        return [
            ComplexS.from_orm(o_).dict()
            for o_ in obj
        ]
    else:
        return ComplexS.from_orm(obj).dict()
