from abc import ABC, abstractmethod
from pydantic import BaseModel


class BaseTextClass(BaseModel):
    table_schema: str
    column_descriptions: str = None
    description_text: str = "Following are some descriptions for column names"

    @property
    def config_text(self) -> str:
        return "You are a natural language model that can generate SQL queries for given input text.\n\
If you are able to provide the SQL query, start the response with number 200, give a space and then the sql query.\n\
If you are not able to provide the sql query, start the response with number 500, give a space and then give the reason\
you cannot provide the sql query, without giving any information about the table attributes.\n\
Following is the Table creation data.\n"
