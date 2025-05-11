from src.datascience_project import logger
from src.datascience_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience_project.pipeline.data_validation_pipeline import DataValidationPipeline
from src.datascience_project.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.datascience_project.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.datascience_project.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
STAGE_NAME = "Data Ingestion stage"

logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

try:
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
except Exception as e:
    logger.exception(e)
    raise e

logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")


STAGE_NAME = "Data Validation stage"

logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

try:
    data_validation = DataValidationPipeline()
    data_validation.initiate_data_validation()
except Exception as e:
    logger.exception(e)
    raise e

logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")


STAGE_NAME = "Data Transformation stage"

logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

try:
    data_transformation = DataTransformationPipeline()
    data_transformation.initiate_data_transformation()
except Exception as e:
    logger.exception(e)
    raise e

logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")


STAGE_NAME = "Model Trainer stage"

logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

try:
    model_trainer = ModelTrainerPipeline()
    model_trainer.initiate_model_trainer_pipeline()
except Exception as e:
    logger.exception(e)
    raise e

logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")


STAGE_NAME = "Model Evaluation stage"

logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

try:
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.initiate_model_evaluation()
except Exception as e:
    logger.exception(e)
    raise e

logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")