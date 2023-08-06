from pydantic import BaseModel


class Factsheet(BaseModel):
    client: str
    budget: str
    timeframe: str
    sc_required: bool
    status: str
