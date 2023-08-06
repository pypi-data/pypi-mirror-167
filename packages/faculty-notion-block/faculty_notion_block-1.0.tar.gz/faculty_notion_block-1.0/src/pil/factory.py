import json
import os

from pil.lib.api import PageBuilder
from pil.lib.blocks import *  # noqa
from pil.lib.utils import get_input_data
from pil.schemas import (
    Bookmark,
    Callout,
    CodeRepoTemplate,
    DetailsTemplate,
    GoogleDriveTemplate,
    InputDataTemplate,
    LessonsLearnedTemplate,
    SimpleTableTemplate,
)


class Factory:
    def __init__(self, notion_api: str) -> None:
        self.pb = PageBuilder(notion_api)
        self.divider = make_divider()
        self.callout = make_callout()
        self.bookmark = make_bookmark(url="")

    def _add_breadcrumb(self):
        # Add breadcrumb
        breadcrumb = make_breadcrumb()
        self.pb.add_block(breadcrumb)

    def _add_version_control(self):
        # Add version line
        version_control = make_paragraph(
            content="Project Information Log (PIL💊) version v2.1"
        )
        self.pb.add_block(version_control)

    @validate_arguments
    def _grab_bookmark(self, data: Bookmark):
        if data["url"] == "":
            return self.bookmark
        else:
            return make_bookmark(url=data["url"], caption=data["caption"])

    @validate_arguments
    def _grab_callout(self, data: Callout):
        if data["content"] == "":
            return self.callout
        else:
            return make_callout(
                content=data["content"],
                emoji=data["emoji"],
                color=data["color"],
            )

    def _make_header(self):
        self._add_breadcrumb()
        self._add_version_control()

    def _make_problem_row(self) -> HeaderBlock:
        paragraph_problem = make_paragraph(
            content="What is the problem that the customer would like to solve? [🧪⚙️]"
        )

        header_problem = make_header(
            content="❓Problem",
            type=3,
            children=[paragraph_problem, self.callout],
        )

        return header_problem

    def _make_solution_row(self) -> HeaderBlock:
        paragraph_solution_1 = make_paragraph(
            content="What steps did the DS team take to address the problem? [🧪]"
        )
        paragraph_solution_2 = make_paragraph(
            content="How did the MLE team provide support to the solution? [⚙️]"
        )
        header_solution = make_header(
            content="📝 Solution",
            type=3,
            children=[
                paragraph_solution_1,
                self.callout,
                paragraph_solution_2,
                self.callout,
            ],
        )

        return header_solution

    def _make_deliverable_row(self) -> HeaderBlock:
        paragraph_deliverable = make_paragraph(
            content="What are the deliverables? [🧪⚙️]"
        )

        header_problem = make_header(
            content="🎁 Deliverables",
            type=3,
            children=[paragraph_deliverable, self.callout],
        )

        return header_problem

    def _make_first_column(self):
        # Construct project summary column
        project_summary_header = make_header(content="Project Summary", type=2)

        description_1 = make_paragraph(
            content="Please provide a concise summary for the following attributes. For example, what approaches were used, which libraries, techniques, etc"
        )
        description_2 = make_paragraph(content="[🧪=DS ⚙️=MLE]")

        # Project Summary - Problem
        header_problem = self._make_problem_row()

        # Project Summary - Solution
        header_solution = self._make_solution_row()

        # Project Summary - Deliverables
        header_deliverables = self._make_deliverable_row()

        column_1_blocks = [
            project_summary_header,
            self.divider,
            description_1,
            description_2,
            header_problem,
            header_solution,
            header_deliverables,
        ]

        return column_1_blocks

    def _make_second_column(self):
        # Construct factsheet column
        factsheet_header = make_header(content="🖌 Factsheet", type=2)

        column_2_blocks = [factsheet_header, self.divider]
        return column_2_blocks

    @validate_arguments
    def _add_simple_table_to_column(self, response, data: SimpleTableTemplate):

        response_json = json.loads(response.text)

        # Retrieve the block ID of column list
        column_list_block_id = response_json["results"][-2]["id"]

        # Retrieve the block ID of 2nd column within column list
        response = self.pb.retrieve_page_block(block_id=column_list_block_id)
        response_json = json.loads(response.text)
        column_2_id = response_json["results"][1]["id"]

        # create the fact table
        fact_table = make_table(
            table_width=2,
            row_cells=[
                make_table_row_block(
                    column_cells=[
                        [make_column_cell(content="Client")],
                        [make_column_cell(content=data["client"])],
                    ]
                ),
                make_table_row_block(
                    column_cells=[
                        [make_column_cell(content="Budget")],
                        [make_column_cell(content=data["budget"])],
                    ]
                ),
                make_table_row_block(
                    column_cells=[
                        [make_column_cell(content="Timeframe")],
                        [make_column_cell(content=data["timeframe"])],
                    ]
                ),
                make_table_row_block(
                    column_cells=[
                        [make_column_cell(content="SC required")],
                        [make_column_cell(content=data["sc_required"])],
                    ]
                ),
                make_table_row_block(
                    column_cells=[
                        [make_column_cell(content="Status")],
                        [make_column_cell(content=data["status"])],
                    ]
                ),
            ],
            has_row_header=True,
        )
        self.pb.add_block(fact_table)

        # append the table to the second column
        response = self.pb.append_blocks_to_page(column_2_id)

    def _make_finance_database(self, page_id: str, data: InputDataTemplate):
        # Add finance block
        response = self.pb.add_inline_database_to_page(page_id)

        # # Populate finance data
        response_json = json.loads(response.text)

        self.pb.add_data_to_database(
            database_id=response_json["id"],
            data=get_input_data(key="database", dictionary=data),
        )

        self.pb.add_block(self.divider)

    @validate_arguments
    def _make_code_repo(self, data: CodeRepoTemplate):
        # Code repo block
        paragraph_repo = make_paragraph(
            content="Please provide the link to the source code (if any)."
        )

        header_repo = make_header(
            content="🗄 Code Repository",
            type=3,
            children=[
                paragraph_repo,
                self._grab_bookmark(data["link"]),
            ],
        )
        return header_repo

    @validate_arguments
    def _make_GD(self, data: GoogleDriveTemplate):

        # Reports and slides folder
        paragraph_reports = make_paragraph(content="📖 Report & Slides")

        # Proposals folder
        paragraph_proposals = make_paragraph(content="💬 Proposals")

        # Others folder
        paragraph_others = make_paragraph(content="Others")

        # Google Drive folder
        paragraph_gd = make_paragraph(
            content="Please provide the link to the Google Drive folder."
        )
        header_gd = make_header(
            content="🗂 Google Drive folder",
            type=3,
            children=[
                paragraph_gd,
                self._grab_bookmark(data["link"]),
                paragraph_reports,
                self._grab_bookmark(data["reports"]),
                paragraph_proposals,
                self._grab_bookmark(data["proposals"]),
                paragraph_others,
                self._grab_bookmark(data["others"]),
            ],
        )
        return header_gd

    @validate_arguments
    def _make_lessons_learned(self, data: LessonsLearnedTemplate):
        # Lessons learned block
        paragraph_lessons = make_paragraph(
            content="What worked or didn’t worked well? [🧪⚙️]"
            + "\nWhat would you do differently? [🧪⚙️]"
        )
        header_lessons = make_header(
            content="🎒 Lessons Learned",
            type=3,
            children=[
                paragraph_lessons,
                self._grab_callout(data["callout"]),
            ],
        )
        return header_lessons

    @validate_arguments
    def _make_details_section(self, data: DetailsTemplate):

        # Repo section
        header_repo = self._make_code_repo(data["code_repo"])

        header_gd = self._make_GD(data["gd"])

        header_lessons = self._make_lessons_learned(data["lessons_learned"])

        # Details block
        header_details = make_header(
            content="Details",
            type=2,
            children=[header_repo, header_lessons, header_gd],
        )

        self.pb.add_block(header_details)

    @validate_arguments
    def add_pil(self, page_id, data: InputDataTemplate):

        self._make_header()

        # Construct blocks for 1st column
        column_1_blocks = self._make_first_column()
        # Construct blocks for 2nd column
        column_2_blocks = self._make_second_column()

        # Construct column list
        column_list = make_column_list(
            column_1=column_1_blocks, column_2=column_2_blocks
        )

        # Append blocks
        self.pb.add_block(column_list)
        self.pb.add_block(self.divider)
        """
        Add the blocks to page first and retrieve the block ID.
        At the moment of writing, the Notion API only support
        text related template creation (i.e. headings, paragraphs,
        etc) and does not support constructing simple table, databases
        in template style. The only way to do it is to create the table
        and then append to the column blocks with its block ID. Hence the
        function below first flush and append the blocks to Notion. It then
        retrieves the block ID of the column list for the simple table
        to append to.
        """
        response = self.pb.append_blocks_to_page(page_id)

        # Append simple table to 2nd column
        self._add_simple_table_to_column(response, data["simple_table"])

        # Create finance datbase
        self._make_finance_database(page_id=page_id, data=data)

        # Add details section
        self._make_details_section(data["details"])

        # Build PIL💊 template
        response = self.pb.append_blocks_to_page(block_id=page_id)


if __name__ == "__main__":
    notion_api = os.getenv("VITE_NOTION_API")
    factory = Factory(notion_api)
    page_id = "8267028a09cc4052b9ef7abf4baabf1a"
    # page_id = "3afac567c2e247d6a32e162c63676afa"
    dummy_data = {
        "simple_table": {
            "client": "Home Office",
            "budget": "£194k",
            "timeframe": "12 weeks",
            "sc_required": "Yes",
            "status": "Completed",
        },
        "database": [
            {
                "guild": "DS",
                "project_members": [
                    # {
                    #     "email": "arnaud.leredde@faculty.ai",
                    #     "id": "d05e429b-3af0-4fa1-9328-f18321e6fa16",
                    # },
                    # {
                    #     "id": "7c1c8075-7e5f-42d1-9b90-001f171896a5",
                    #     "email": "george.prichard@faculty.ai",
                    # },
                ],
                "cost_booked": 35,
                "time_booked": 84,
            },
            {
                "guild": "MLE",
                "project_members": [
                    # {
                    #     "id": "7c1c8075-7e5f-42d1-9b90-001f171896a5",
                    #     "email": "george.prichard@faculty.ai",
                    # },
                ],
                "cost_booked": 152,
                "time_booked": 126,
            },
        ],
        "details": {
            "code_repo": {"link": {"url": "www.google.com", "caption": ""}},
            "lessons_learned": {
                "callout": {"content": "Example Callout", "color": "red"}
            },
            "gd": {
                "link": {"url": "www.google.com1"},
                "reports": {"url": "www.google.com2"},
                "proposals": {"url": "www.google.com3", "caption": ""},
                "others": {"url": "www.google.com4", "caption": "A Caption"},
            },
        },
    }

    factory.add_pil(page_id, data={})
