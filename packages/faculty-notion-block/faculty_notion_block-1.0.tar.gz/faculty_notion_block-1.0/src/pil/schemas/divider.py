from pil.schemas.general import Block


class DividerBlock(Block):
    type: str = "divider"
    divider: dict = {}
