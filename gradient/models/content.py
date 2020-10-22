from pydantic import BaseModel


class ContentResult(BaseModel):
    _id: int
    _name: str
    _pct: str
    _prior_week: str
    _date: str