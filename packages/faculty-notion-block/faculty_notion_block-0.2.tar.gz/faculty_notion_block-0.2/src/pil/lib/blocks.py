from pydantic import Field, validate_arguments
from pydantic.typing import Annotated

from pil.schemas import (
    Annotations,
    Block,
    BookMarkAttributes,
    BookmarkBlock,
    BreadCrumbBlock,
    Callout,
    CalloutBlock,
    Caption,
    ColumnAttribute,
    ColumnBlock,
    ColumnCellBlock,
    ColumnList,
    ColumnListBlock,
    Content,
    DatabaseBlock,
    DatabaseColumn,
    DividerBlock,
    Emoji,
    Format,
    Header,
    HeaderBlock,
    Number,
    Option,
    Options,
    Paragraph,
    ParagraphBlock,
    ParentAttribute,
    People,
    PrimaryKeyTitle,
    RichText,
    Selection,
    SimpleTableBlock,
    TableAttributes,
    TableRowBlock,
    TableRowCell,
)


def make_column_list(column_1: list[Block], column_2: list[Block]) -> ColumnListBlock:
    """Make column view with 2 columns in a page. Hardcoded to be 2 for now.

    Args:
        column_1 (list[Block]): The list of blocks within first column
        column_2 (list[Block]): The list of blocks within second column

    Returns:
        ColumnListBlock: The column list block object
    """
    column_block_1 = ColumnBlock(column=ColumnAttribute(children=column_1))
    column_block_2 = ColumnBlock(column=ColumnAttribute(children=column_2))
    column_list = ColumnList(children=[column_block_1, column_block_2])
    column_list_block = ColumnListBlock(column_list=column_list)
    return column_list_block.dict()


def make_paragraph(content: str) -> ParagraphBlock:
    """Make a paragraph block

    Args:
        content (str): Text content to be included for the paragraph

    Returns:
        ParagraphBlock: Paragraph block object
    """
    txt_content = Content(content=content)
    rich_txt = RichText(text=txt_content)
    paragraph = Paragraph(rich_text=[rich_txt])
    block = ParagraphBlock(paragraph=paragraph)
    return block.dict()


def make_callout(
    content: str = "", emoji: str = "✏️", color: str = "gray_background"
) -> CalloutBlock:
    """Make a callout block

    Args:
        content (str, optional): Text content. Defaults to "".
        emoji (str, optional): Emoji for the callout. Defaults to "✏️".
        color (str, optional): color of callout background.
        Defaults to "gray_background".

    Returns:
        CalloutBlock: Callout block object
    """
    txt_content = Content(content=content)
    rich_txt = RichText(text=txt_content)
    callout = Callout(rich_text=[rich_txt], icon=Emoji(emoji=emoji), color=color)
    block = CalloutBlock(callout=callout)
    return block.dict()


@validate_arguments
def make_header(
    content: str,
    type: Annotated[int, Field(gt=0, le=3)] = 1,
    color="default",
    children: list[object] = [],
) -> HeaderBlock:
    """Make different header blocks

    Args:
        content (str): Text content.
        type (Annotated[int, Field, optional): Heading type (1 - 3). Defaults to 1.
        color (str, optional): Text colour. Defaults to "default".
        children (list[object], optional): Children of the block. Defaults to empty.

    Returns:
        HeaderBlock: Header block object
    """

    txt_content = Content(content=content)
    rich_txt = RichText(text=txt_content)
    header = Header(rich_text=[rich_txt], color=color, children=children)
    header_type = f"heading_{type}"
    block = HeaderBlock(type=header_type)
    # Dynamically inject the header_tpye attribute to support header_{x}
    setattr(block, header_type, header)
    return block.dict()


def make_column_cell(
    content: str,
    annotations: Annotations = Annotations(),
    link: str = None,
    href: str = None,
) -> ColumnCellBlock:
    """Make column cells

    Args:
        content (str): Text content.
        annotations (Annotations, optional): Text annotations.
        Defaults to Annotations().
        link (str, optional): Specify a link. Defaults to None.
        href (str, optional): Specify a link. Defaults to None.

    Returns:
        ColumnCellBlock: Column cell block
    """
    txt_content = Content(content=content, link=link)
    column_cell = ColumnCellBlock(text=txt_content, annotations=annotations, href=href)
    return column_cell.dict()


def make_table_row_block(column_cells: list[list[ColumnCellBlock]]) -> TableRowBlock:
    """Make table rows

    Args:
        column_cells (list[list[ColumnCellBlock]]): A collection of column cell blocks

    Returns:
        TableRowBlock: Table row block
    """
    table_row_cell = TableRowCell(cells=column_cells)
    table_row = TableRowBlock(table_row=table_row_cell)
    return table_row.dict()


def make_table(
    table_width: int,
    row_cells: list[TableRowBlock],
    has_column_header=False,
    has_row_header=False,
) -> SimpleTableBlock:
    """Make a simple table block

    Args:
        table_width (int): The number of columns of the table.
        row_cells (list[TableRowBlock]): Define the list of rows in the table.
        has_column_header (bool, optional): Highlight first row. Defaults to False.
        has_row_header (bool, optional): Highlight first column. Defaults to False.

    Returns:
        SimpleTableBlock: Simple table object
    """
    tb = TableAttributes(
        table_width=table_width,
        has_column_header=has_column_header,
        has_row_header=has_row_header,
        children=row_cells,
    )
    simplt_table = SimpleTableBlock(table=tb)
    return simplt_table.dict()


def make_divider() -> DividerBlock:
    """Make a divider

    Returns:
        DividerBlock: Divider block object.
    """
    divider = DividerBlock()
    return divider.dict()


def make_breadcrumb() -> BreadCrumbBlock:
    """Make breadcrumb.

    Returns:
        BreadCrumbBlock: Breadcrumb object.
    """
    breadcrumb = BreadCrumbBlock()
    return breadcrumb.dict()


def make_bookmark(url: str = "", caption: str = "") -> BookmarkBlock:
    """Make bookmark

    Args:
        url (str, optional): url of the bookmark. Defaults to empty.
        caption (str, optional): caption for the url. Defaults to empty.

    Returns:
        BookmarkBlock: Bookmark object
    """
    content = Content(content=caption)
    caption = Caption(text=content, annotations=Annotations())
    bma = BookMarkAttributes(url=url, caption=[caption])
    bookmark = BookmarkBlock(bookmark=bma)
    print(bookmark.dict())
    return bookmark.dict()


def make_database(page_id: str) -> DatabaseBlock:
    """To create an inline database within a page

    Args:
        page_id (str): Page ID of where the database is located

    Returns:
        DatabaseBlock: Inline database object.
    """
    option_1 = Option(name="MLE", color="green")
    option_2 = Option(name="DS", color="red")
    option_3 = Option(name="Commercial", color="yellow")
    options = Options(options=[option_1, option_2, option_3])
    properties = DatabaseColumn(
        project_members=People(),
        guild=Selection(select=options),
        time_booked=Number(),
        cost_booked=Number(number=Format(format="pound")),
        primary_key=PrimaryKeyTitle(),
    )
    database_title = [RichText(text=Content(content="Finance Info"))]
    parent = ParentAttribute(page_id=page_id)
    database = DatabaseBlock(parent=parent, title=database_title, properties=properties)
    return database.dict()
