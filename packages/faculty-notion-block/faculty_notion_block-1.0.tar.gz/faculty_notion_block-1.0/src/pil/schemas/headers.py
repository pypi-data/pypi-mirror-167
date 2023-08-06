from pydantic import BaseModel, Extra

from pil.schemas.general import Block, RichText


class Emoji(BaseModel):
    emoji: str


class Header(BaseModel):
    rich_text: list[RichText]
    is_toggleable: bool = False
    color: str
    children: object


class HeaderBlock(Block, extra=Extra.allow):
    type: str
