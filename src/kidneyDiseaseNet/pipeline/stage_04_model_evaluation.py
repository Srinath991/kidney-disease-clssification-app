from kidneyDiseaseNet.config.configuration import ConfigurationManager
from kidneyDiseaseNet.components.model_evaluation_mlflow import Evaluation
from kidneyDiseaseNet import logger


STAGE_NAME = "mlflow Evaluation"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()