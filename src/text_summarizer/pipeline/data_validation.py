from text_summarizer.logging import logger
from text_summarizer.components.data_validation import DataValidation


class DataValidationPipeline:
    def __init__(self, config):
        self.config = config

    def run(self):
        data_ingestion_config = self.config.get_data_validation_config()
        data_ingestion = DataValidation(data_ingestion_config)
        return data_ingestion.validate()