from typing import Optional

from pydantic import BaseModel


class SimpleTableTemplate(BaseModel):
    client: Optional[str] = ""
    budget: Optional[str] = ""
    timeframe: Optional[str] = ""
    sc_required: Optional[str] = ""
    status: Optional[str] = ""

    def __getitem__(self, item):
        return getattr(self, item)


class NotionPerson(BaseModel):
    type: str = "person"
    person: dict
    id: str

    def __getitem__(self, item):
        return getattr(self, item)


class Person(BaseModel):
    email: str
    id: str

    def __getitem__(self, item):
        return getattr(self, item)


class DatabaseTemplate(BaseModel):
    guild: Optional[str] = ""
    project_members: Optional[list[Person]] = ""
    cost_booked: Optional[str] = ""
    time_booked: Optional[str] = ""

    def __getitem__(self, item):
        return getattr(self, item)


class Bookmark(BaseModel):
    url: str = ""
    caption: Optional[str] = ""

    def __getitem__(self, item):
        return getattr(self, item)


class Callout(BaseModel):
    content: str = ""
    emoji: Optional[str] = "✏️"
    color: Optional[str] = "default"

    def __getitem__(self, item):
        return getattr(self, item)


class GoogleDriveTemplate(BaseModel):
    link: Optional[Bookmark] = Bookmark()
    reports: Optional[Bookmark] = Bookmark()
    proposals: Optional[Bookmark] = Bookmark()
    others: Optional[Bookmark] = Bookmark()

    def __getitem__(self, item):
        return getattr(self, item)


class CodeRepoTemplate(BaseModel):
    link: Optional[Bookmark] = ""

    def __getitem__(self, item):
        return getattr(self, item)


class LessonsLearnedTemplate(BaseModel):
    callout: Callout = Callout()

    def __getitem__(self, item):
        return getattr(self, item)


class DetailsTemplate(BaseModel):
    code_repo: CodeRepoTemplate = CodeRepoTemplate()
    lessons_learned: LessonsLearnedTemplate = LessonsLearnedTemplate()
    gd: GoogleDriveTemplate = GoogleDriveTemplate()

    def __getitem__(self, item):
        return getattr(self, item)


class InputDataTemplate(BaseModel):
    simple_table: Optional[SimpleTableTemplate] = SimpleTableTemplate()
    database: Optional[DatabaseTemplate] = DatabaseTemplate()
    details: Optional[DetailsTemplate] = DetailsTemplate()

    def __getitem__(self, item):
        return getattr(self, item)


# {
# 	"simple_table": {
# 		"client": "",
# 		"budget": "",
# 		"timeframe": "",
# 		"sc_required": "",
# 		"status": ""
# 	},
# 	"database": [{
# 		"guild": [],
# 		"project_members": [],
# 		"cost_booked": [],
# 		"time_booked": []
# 	}],
# 	"details": {
# 		"code_repo": {
# 			"link": ""
# 		},
# 		"lessons_learned": "",
# 		"gd": {
# 			"link": "",
# 			"reports": "",
# 			"proposals": "",
# 			"others": ""
# 		}
# 	}
# }
