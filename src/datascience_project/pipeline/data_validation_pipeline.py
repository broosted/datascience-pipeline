from src.datascience_project.config.configuration import ConfigurationManager
from src.datascience_project.components.data_validation import DataValidation
from src.datascience_project import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass
    
    def initiate_data_validation(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        
        