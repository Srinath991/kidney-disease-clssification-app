from kidneyDiseaseNet.config.configuration import ConfigurationManager
from kidneyDiseaseNet.components.model_training import Training
from kidneyDiseaseNet import logger


STAGE_NAME = "Model trainning"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        
        
    