from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_validation import DataValiadtion
from src.mlProject.components.data_transformation import DataTransformation
from src.mlProject.components.model_training import ModelTrainer
from src.mlProject import logger



STAGE_NAME = "Model Training stage"

class modelTrainingPipeline:
    def __init__(self):
        pass
     
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
        
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = modelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e                