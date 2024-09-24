import tensorflow as tf 
from tensorflow import keras

model=tf.keras.models.load_model('artifacts/training/final_model.h5')
test_datagen=tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1/255
)
test_data=test_datagen.flow_from_directory(
    directory='artifacts/data_ingestion/test',
    target_size=(224,224),
    class_mode='categorical',
    batch_size=32
    
)

model.evaluate(test_data)