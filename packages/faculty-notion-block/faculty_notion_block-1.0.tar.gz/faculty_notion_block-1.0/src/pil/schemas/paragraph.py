from pydantic import BaseModel

from pil.schemas.general import Block, RichText


class Paragraph(BaseModel):
    rich_text: list[RichText]
    color: str = "default"


class ParagraphBlock(Block):
    type: str = "paragraph"
    paragraph: Paragraph
