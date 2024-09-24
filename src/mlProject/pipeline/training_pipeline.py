from mlProject.components.data_ingestion import DataIngestion
from mlProject.components.prepare_base_model import BaseModel
from mlProject import logging
from mlProject.config.configuration import Configurationmanger

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try: 
            config=Configurationmanger()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.Download_file()
            data_ingestion.Extract_Data()
            
        except Exception as e:
            logging.exception(e)
            raise e     
        
class BaseModelPipeline:       
    
    def __init__(self) -> None:
        pass 
        
    def main(self):
        try:
            config=Configurationmanger()
            preapre_base_model_config=config.get_prepare_base_model_config()
            preapre_base_model=BaseModel(config=preapre_base_model_config)
            preapre_base_model.transferlearning_model()
            
        except Exception as e:
            logging.exception(e)
            raise e 
        