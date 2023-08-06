from pydantic import BaseModel


class Content(BaseModel):
    content: str
    link: str | None = None


class RichText(BaseModel):
    type: str = "text"
    text: Content


class Annotations(BaseModel):
    bold: bool = False
    italic: bool = False
    strikethrough: bool = False
    underline: bool = False
    code: bool = False
    color: str = "default"


class Block(BaseModel):
    type: str
