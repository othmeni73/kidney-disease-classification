from cnnDiseaseClassifier import logger
from cnnDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline # type: ignore
from cnnDiseaseClassifier.pipeline.stage_03_training import TrainingPipeline
from cnnDiseaseClassifier.pipeline.stage_04_evaluate_model import EvaluatePipeline
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


STAGE_NAME="training stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<")
    training = TrainingPipeline()
    training.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed  <<<<<<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluate model stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<")
        model_evaluation = EvaluatePipeline()
        model_evaluation.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed  <<<<<<<<<")
       
    except Exception as e:
        logger.exception(e)
        raise e