from chestCancer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chestCancer import logger
from chestCancer.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from chestCancer.pipeline.stage_03_model_trainer import ModelTrainerPipleline

STAGE_NAME = "Data Ingestion stage"


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    


STAGE_NAME = "Prepare Base Model stage"


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Trainer stage"


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipleline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    