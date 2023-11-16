from text_summarizer.logging import logger
from text_summarizer.components.data_ingestion import DataIngestion


class DataIngestionPipeline:
    def __init__(self, config):
        self.config = config

    def run(self):
        data_ingestion_config = self.config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_files()