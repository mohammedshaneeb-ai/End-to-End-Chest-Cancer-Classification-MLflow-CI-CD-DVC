from chestCancer.config.configuration import ConfigurationManager
from chestCancer.components.model_trainer import ModelTraining
from chestCancer import logger


STAGE_NAME = "Model Trainer stage"

class ModelTrainerPipleline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = ModelTraining(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipleline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e