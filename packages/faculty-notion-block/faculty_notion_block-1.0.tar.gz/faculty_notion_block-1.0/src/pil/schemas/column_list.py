from pydantic import BaseModel

from pil.schemas.general import Block


class ColumnAttribute(BaseModel):
    children: list[object]


class ColumnBlock(Block):
    type: str = "column"
    column: ColumnAttribute


class ColumnList(BaseModel):
    children: list[ColumnBlock]


class ColumnListBlock(Block):
    type: str = "column_list"
    column_list: ColumnList
