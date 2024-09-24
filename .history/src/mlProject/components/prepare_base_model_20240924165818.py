from mlProject.config.configuration import *
from mlProject import logger
import tensorflow as tf 
from tensorflow import keras


class BaseModel:
    def __init__(self,config:BaseModelConfig) -> None:
        self.config=config
        
    def transferlearning_model(self):
        try:
            self.model=tf.keras.applications.VGG16(
                include_top=False,
                input_shape=(224,224,3),
                weights='imagenet'
            )
            
            for layer in self.model.layers:
                layer.trainable=False
                
            model=tf.keras.layers.Flatten()(self.model.output)
            predict_layer=tf.keras.layers.Dense(units=3,activation='softmax')(model)
            
            model=tf.keras.Model(inputs=self.model.input,outputs=predict_layer)
            
            model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
            
            model.summary()
            
            model.save(self.config.vgg_model)
            
        except Exception as e:
            logging.exception(e) 
            raise e   