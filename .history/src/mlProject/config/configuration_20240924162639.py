from mlProject.entity.config_entity import *
from mlProject import logging
from mlProject.utils.common import read_yaml,create_directories
from mlProject.constants import *

class Configurationmanger:
    def __init__(self) -> None:
        self.config=read_yaml(CONFIG_FILE_PATH)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self):
        config=self.config.data_ingestion
        
        create_directories([config.roo_dir])
        
        data_ingestion_config=DataIngestionConfig(
            roo_dir=config.roo_dir,
            URL=config.URL,
            locat_data_path=config.locat_data_path,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config