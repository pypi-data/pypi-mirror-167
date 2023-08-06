from pydantic import BaseModel

from pil.schemas.general import Block, RichText


class Emoji(BaseModel):
    emoji: str


class CalloutAttributes(BaseModel):
    rich_text: list[RichText]
    icon: Emoji
    color: str


class CalloutBlock(Block):
    type: str = "callout"
    callout: CalloutAttributes
