from src.TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.TextSummarizer.logging import logger
from src.TextSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from src.TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.TextSummarizer.pipeline.stage_04_model_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion Pipeline"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX=============X")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data validation Pipeline"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX=============X")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Pipeline"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX=============X")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Training Pipeline"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX=============X")

except Exception as e:
    logger.exception(e)
    raise e