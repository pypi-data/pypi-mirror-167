from pil.schemas.general import Block


class BreadCrumbBlock(Block):
    type: str = "breadcrumb"
    breadcrumb: dict = {}
