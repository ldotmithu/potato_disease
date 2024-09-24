from mlProject.components.data_ingestion import DataIngestion
from mlProject import logging
from mlProject.config.configuration import Configurationmanger

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=Configurationmanger()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.Download_file()
        data_ingestion.Extract_Data()