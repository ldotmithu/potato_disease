from mlProject.config.configuration import *
from mlProject import logging
import zipfile,os
import gdown


class DataIngestion:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config =config
        
    def Download_file(self):
        try:
            url=self.config.URL
            zip_dir=self.config.locat_data_path
            os.makedirs(self.config.root_dir,exist_ok= True)    
            
            id=url.split('/')[-2]
            prefix= 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+id,zip_dir)
            logging.info('Download Zip data')
            
        except Exception as e:
            logging.exception(e)
            raise e
        
    def Extract_Data(self):
        unzip_Path=self.config.unzip_dir
        os.makedirs(unzip_Path,exist_ok=True)
        with zipfile.ZipFile(self.config.locat_data_path,'r') as f:
            f.extractall(unzip_Path)
            logging.info('Data Extract Succesfull')