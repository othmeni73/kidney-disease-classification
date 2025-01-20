from cnnDiseaseClassifier.entity.config_entity  import (DataIngestionConfig,PrepareBaseModelConfig,TrainModelConfig)
from cnnDiseaseClassifier.constants import *
from cnnDiseaseClassifier.utils.common import read_yaml, create_directories

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath= PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params =  read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir

        )
        return data_ingestion_config
    
    def get_prepare_base_model_config(self)->PrepareBaseModelConfig:
        config =self.config.prepare_base_model
        create_directories([config.root_dir])
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_base_model_path = Path(config.updated_base_model_path),
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate = self.params.LEARNING_RATE,
            params_incluse_top = self.params.INCLUDE_TOP,
            params_weights = self.params.WEIGHTS,
            params_classes= self.params.CLASSES
        )
        return prepare_base_model_config
    
    def get_training_config(self) ->TrainModelConfig:
        config=self.config.training
        base_model_config = self.config.prepare_base_model
        training_data = os.path.join(self.config.data_ingestion.unzip_dir,"kidney-ct-scan-image")

        create_directories([Path(config.root_dir)])

        training_config = TrainModelConfig(
            root_dir = Path(config.root_dir),
            trained_model_path = Path(config.trained_model_path), 
            updated_base_model_path = Path(base_model_config.updated_base_model_path), 
            training_data = Path(training_data), 
            params_epochs =  self.params.EPOCHS,
            params_batch_size = self.params.BATCH_SIZE,
            params_is_augmentation = self.params.AUGMENTATION, 
            params_image_size = self.params.IMAGE_SIZE 

        )
        return training_config