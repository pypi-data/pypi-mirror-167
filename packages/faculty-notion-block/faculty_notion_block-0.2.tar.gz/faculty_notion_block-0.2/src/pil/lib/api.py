import json
import logging
import os

# import requests
from pil.lib.blocks import make_database

# from utils import requests_retry_session
from .rest_handler import RestHandler

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(levelname)s:%(message)s",
    level=logging.DEBUG,
)


class PageBuilder:
    def __init__(self, notion_api: str):
        """This class allows blocks to be added and
        pushed to Notion pages. Notion API keys are
        required.

        Args:
            notion_api (str): Notion API key
        """

        # Initialise the rest handler object
        self.rest_handler = RestHandler(notion_api)

        # Initiliase an empty blocks list for the page
        self.blocks = []
        self.notion_url = os.getenv("VITE_NOTION_API_URL")

    def add_block(self, block: object = None) -> bool:
        """Add blocks to the list for bulk creation

        Args:
            block (object, optional): Notion blocks. Defaults to None.

        Returns:
            bool: flag
        """
        self.blocks.append(block)
        return True

    def append_blocks_to_page(self, block_id: str):
        """Bulk creation of blocks to the specified page.

        Args:
            block_id (str): Notion block id

        Returns:
            str: REST response
        """

        response = self.rest_handler.patch(
            url=self.notion_url + f"blocks/{block_id}" + "/children",
            data=json.dumps({"children": self.blocks}),
        )
        response_json = json.loads(response.text)
        logger.debug(response_json)
        # reset block list
        self.blocks = []
        return response

    def add_inline_database_to_page(self, page_id: str):
        """Function to add an inline database to a page.

        Args:
            page_id (str): Notion page ID

        Returns:
            str: REST response
        """

        response = self.rest_handler.post(
            url=self.notion_url + "databases",
            data=json.dumps(make_database(page_id)),
        )
        response_json = json.loads(response.text)
        logger.debug(response_json)
        return response

    def retrieve_page_block(self, block_id: str):
        """Retrieve the children attributes of a block.

        Args:
            block_id (str): Notion block ID

        Returns:
            str: REST response
        """

        response = self.rest_handler.get(
            url=self.notion_url + f"blocks/{block_id}" + "/children",
        )
        response_json = json.loads(response.text)
        logger.debug(response_json)
        return response


# if __name__ == "__main__":
#     notion_api = os.getenv("VITE_NOTION_API")
#     pb = PageBuilder(notion_api)
#     pb.add_block(block=make_divider())
#     pb.append_blocks_to_page("8267028a09cc4052b9ef7abf4baabf1a")
#     # pb.add_inline_database_to_page(page_id="8267028a09cc4052b9ef7abf4baabf1a")
