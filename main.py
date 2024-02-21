from src.TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.TextSummarizer.logging import logger
from src.TextSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline


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
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX=============X")

except Exception as e:
    logger.exception(e)
    raise e
