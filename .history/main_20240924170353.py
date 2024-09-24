from mlProject.pipeline.training_pipeline import DataIngestionPipeline,BaseModelPipeline
from mlProject import logging

Stage_Name='Data Ingestion '
try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.ingestion_main()
    logging.info(f'{Stage_Name} completed')
    logging.info('>>>>>>>>>>>>>>>>>>>>>>>>')
except Exception as e:
    logging.exception(e)
    raise e    
    
Stage_Name='Base Model '
try:
    preapre_base_model=BaseModelPipeline()
    preapre_base_model.ingestion_main()
    logging.info(f'{Stage_Name} completed')
    logging.info('>>>>>>>>>>>>>>>>>>>>>>>>')
except Exception as e:
    logging.exception(e)
    raise e    
        