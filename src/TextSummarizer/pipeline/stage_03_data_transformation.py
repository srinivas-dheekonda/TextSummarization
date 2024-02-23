from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.logging import logger
from TextSummarizer.conponents.data_transformation import DataTransformation







class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
