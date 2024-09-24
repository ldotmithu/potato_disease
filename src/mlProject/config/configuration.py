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
        
        create_directories([config.root_dir])
        
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            URL=config.URL,
            locat_data_path=config.locat_data_path,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config
    
    def get_prepare_base_model_config(self):
        config=self.config.preapre_base_model
        
        create_directories([config.root_dir])
        
        preapre_base_model_config=BaseModelConfig(
            root_dir=config.root_dir,
            vgg_model=config.vgg_model
        )
        return preapre_base_model_config
    
    def get_training_config(self):
        config=self.config.training
        
        create_directories([config.root_dir])
        
        
        training_config=Trainconfig(
            root_dir=config.root_dir,
            vgg_model=config.vgg_model,
            final_model=config.final_model,
            test_data=config.test_data,
            train_data=config.train_data,
            val_data=config.val_data
        )
        
        return training_config