from cnnDiseaseClassifier import logger
from cnnDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline # type: ignore
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed  <<<<<<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Prepare base  model stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<")
    prepare_base_model = PrepareBaseModelPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed  <<<<<<<<<")
       
except Exception as e:
    logger.exception(e)
    raise e