import json
import logging
from typing import Tuple

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(levelname)s:%(message)s",
    level=logging.WARNING,
)


class RestHandler:
    def __init__(self, notion_api: str):
        self.notion_header = {
            "Authorization": f"Bearer {notion_api}",
            "Notion-Version": "2022-02-22",
            "Content-Type": "application/json",
        }
        self.session = self._requests_retry_session()

    def patch(self, url: str, data: object):
        try:
            response = self._requests_retry_session().patch(
                url,
                data=data,
                headers=self.notion_header,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(e)
            logger.error(json.loads(response.text))
            return
        return response

    def post(self, url: str, data: object):
        try:
            response = self._requests_retry_session().post(
                url,
                data=data,
                headers=self.notion_header,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(e)
            logger.error(json.loads(response.text))
            return
        return response

    def get(self, url: str):
        try:
            response = self._requests_retry_session().get(
                url,
                headers=self.notion_header,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(e)
            logger.error(json.loads(response.text))
            return
        return response

    def _requests_retry_session(
        self,
        retries: int = 3,
        backoff_factor: float = 0.3,
        status_forcelist: Tuple[int] = (500, 502, 504),
        session: object = None,
    ):
        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session
