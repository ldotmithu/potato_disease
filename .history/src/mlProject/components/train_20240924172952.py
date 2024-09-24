from mlProject.config.configuration import *
from mlProject import logging
import tensorflow as tf 
from tensorflow import keras



class Train:
    def __init__(self,config:Trainconfig) -> None:
        self.config=config
        
    def model_train(self):
        self.model=tf.keras.models.load_model(self.config.vgg_model)
        