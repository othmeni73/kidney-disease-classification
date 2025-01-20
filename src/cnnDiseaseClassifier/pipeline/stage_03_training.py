from cnnDiseaseClassifier.config.configuration import ConfigurationManager
from cnnDiseaseClassifier.components.training import Training
from cnnDiseaseClassifier import logger

    


STAGE_NAME="training stage"
class TrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        training_config=config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed  <<<<<<<<<")
       
    except Exception as e:
        logger.exception(e)
        raise e