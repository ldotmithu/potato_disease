from mlProject.config.configuration import *
from mlProject import logging
import tensorflow as tf 
from tensorflow import keras



class Train:
    def __init__(self,config:Trainconfig) -> None:
        self.config=config
        
    def model_train(self):
        self.model=tf.keras.models.load_model(self.config.vgg_model)
        
        train_datagen=tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1/255,
            rotation_range=0.2,
            zoom_range=0.2,
            fill_mode='nearest',
            horizontal_flip=True
        )
        
        val_datagen=tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1/255
        )
        
        test_datagen=tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1/255
        )
        
        train_data=train_datagen.flow_from_directory(
            directory=self.config.train_data,
            target_size=(224,224),
            class_mode='categorical',
            batch_size=32,
            seed=123    
        )
        
        val_data=val_datagen.flow_from_directory(
            directory=self.config.val_data,
            target_size=(224,224),
            batch_size=32,
            class_mode='categorical'
        )
        
        test_data=test_datagen.flow_from_directory(
            directory=self.config.test_data,
            target_size=(224,224),
            batch_size=32,
            class_mode='categorical'
        )
        
        self.model.fit(train_data,va)
        
        