from cnnDiseaseClassifier.config.configuration import ConfigurationManager
from cnnDiseaseClassifier.components.evaluate_model import Evaluation
from cnnDiseaseClassifier import logger

    


STAGE_NAME="Evaluate model  stage"
class EvaluatePipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        model_evaluation_config = config.get_evaluation_config()
        model_evaluation = Evaluation(config= model_evaluation_config)
        model_evaluation._valid_generator()
        model_evaluation.evaluation()
        model_evaluation.log_into_mlflow()
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<")
        obj = EvaluatePipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed  <<<<<<<<<")
       
    except Exception as e:
        logger.exception(e)
        raise e