from typing import Dict
from .text_classes.text_mondelez_mt_india import MondelezMTIndiaPromptText
from .text_classes.twinings import TwiningsPromptText

PROJECT_TEXT_CLASS_MAP = {
    "mondelez_mt_india": MondelezMTIndiaPromptText,
    "twinings": TwiningsPromptText
}


class InitialText:
    """
    Class that returns initial config text for a particular project
    """

    def __init__(self, project_id) -> None:
        self.text_class = PROJECT_TEXT_CLASS_MAP.get(project_id, None)
        if self.text_class is None:
            raise ValueError(f"There is not project with id {project_id}")

    def get_initial_text(self):
        """
        Returns config text and table schema for 
        """
        text_obj = self.text_class()
        table_schema = text_obj.table_schema
        config_text = text_obj.config_text
        initial_text = f"{config_text}\n{table_schema}"

        if text_obj.column_descriptions is not None:
            desc_text = f"{text_obj.description_text}\n{text_obj.column_descriptions}"
            initial_text = f"{initial_text}\n{desc_text}"
        return initial_text
