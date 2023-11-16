from text_summarizer.logging import logger
from text_summarizer.components.data_ingestion import DataIngestion
from text_summarizer.config_manager import ConfigManager

logger.info("Loading model...")


config  = ConfigManager()

data_ingestion_config = config.get_data_ingestion_config()
d = DataIngestion(data_ingestion_config)

d.get_files()