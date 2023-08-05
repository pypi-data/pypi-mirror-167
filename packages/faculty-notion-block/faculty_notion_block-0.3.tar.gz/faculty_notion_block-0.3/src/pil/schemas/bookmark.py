from pydantic import BaseModel

from pil.schemas.general import Annotations, Block, Content


class Caption(BaseModel):
    type: str = "text"
    text: Content
    annotations: Annotations
    href: str | None


class BookMarkAttributes(BaseModel):
    url: str
    caption: list[Caption]


class BookmarkBlock(Block):
    type: str = "bookmark"
    bookmark: BookMarkAttributes
