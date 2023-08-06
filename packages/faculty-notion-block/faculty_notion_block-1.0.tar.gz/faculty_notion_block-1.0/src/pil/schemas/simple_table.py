from pydantic import BaseModel

from pil.schemas.general import Annotations, Block, Content


class ColumnCellBlock(Block):
    type: str = "text"
    text: Content
    annotations: Annotations
    href: str | None


class TableRowCell(BaseModel):
    cells: list[list[ColumnCellBlock]]


class TableRowBlock(Block):
    type: str = "table_row"
    table_row: TableRowCell


class TableAttributes(BaseModel):
    table_width: int
    has_column_header: bool = False
    has_row_header: bool = False
    children: list[TableRowBlock] | None


class SimpleTableBlock(Block):
    type: str = "table"
    table: TableAttributes
