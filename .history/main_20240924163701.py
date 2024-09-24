from mlProject.pipeline.training_pipeline import DataIngestionPipeline
from mlProject import logging

Stage_Name='Data Ingestion '
try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f'{Stage_Name} completed')
    logging.info('>>>>>>>>>>>>>>>>>>>>>>>>')
except Exception as e:
    logging.exception(E)
    raise e    
    