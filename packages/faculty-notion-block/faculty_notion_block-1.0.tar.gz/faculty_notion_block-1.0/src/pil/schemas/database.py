from pydantic import BaseModel, Field

from pil.schemas.general import RichText


class ParentAttribute(BaseModel):
    type: str = "page_id"
    page_id: str


class People(BaseModel):
    people: dict = {}


class Option(BaseModel):
    name: str
    color: str


class Options(BaseModel):
    options: list[Option]


class Selection(BaseModel):
    select: Options


class Format(BaseModel):
    format: str


class Number(BaseModel):
    number: Format | dict = {}


class PrimaryKeyTitle(BaseModel):
    title: dict = {}


class DatabaseColumn(BaseModel):
    project_members: People = Field(alias="Project Members")
    guild: Selection = Field(alias="Guild")
    time_booked: Number = Field(alias="Time(booked)")
    cost_booked: Number = Field(alias="Cost(booked)")
    primary_key: PrimaryKeyTitle = Field(alias="#")

    class Config:
        allow_population_by_field_name = True


class DatabaseBlock(BaseModel):
    parent: ParentAttribute
    is_inline: bool = True
    title: list[RichText]
    properties: DatabaseColumn
