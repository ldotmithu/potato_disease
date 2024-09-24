from mlProject.pipeline.training_pipeline import DataIngestionPipeline,BaseModelPipeline,TrainPipeline
from mlProject import logging

Stage_Name='Data Ingestion '
try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f'{Stage_Name} completed')
    logging.info('>>>>>>>>>>>>>>>>>>>>>>>>')
except Exception as e:
    logging.exception(e)
    raise e    
    
Stage_Name='Base Model '
try:
    preapre_base_model=BaseModelPipeline()
    preapre_base_model.main()
    logging.info(f'{Stage_Name} completed')
    logging.info('>>>>>>>>>>>>>>>>>>>>>>>>')
except Exception as e:
    logging.exception(e)
    raise e    
        
Stage_Name='Train '
try:
    train=TrainPipeline()
    train.main()
    logging.info(f'{Stage_Name} completed')
    logging.info('>>>>>>>>>>>>>>>>>>>>>>>>')
except Exception as e:
    logging.exception(e)
    raise e    