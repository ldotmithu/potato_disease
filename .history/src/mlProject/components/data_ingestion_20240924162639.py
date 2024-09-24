from mlProject.config.configuration import *
from mlProject import logging
import zipfile,os
import gdown


class DataIngestion:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config =config
        
    def Download_file(self):
        
