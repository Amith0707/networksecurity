import os
import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecuritySystem
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import DataTransformationConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import ModelTrainerConfig

##To know what to import like above just check __init__ of that file and see what it is aslking/demanding to be executed

if __name__=="__main__":
    try:
        trainingPipelineConfig=TrainingPipelineConfig()
        dataIngestionConfig=DataIngestionConfig(trainingPipelineConfig)
        datavalidaitonConfig=DataValidationConfig(trainingPipelineConfig)
        dataIngestion=DataIngestion(dataIngestionConfig)
        logging.info("Initiate the data ingestion")
        data_ingestion_artifact=dataIngestion.initate_data_ingestion()
        logging.info("Data Initiation completed")
        print(data_ingestion_artifact)
        data_validation=DataValidation(data_ingestion_artifact,datavalidaitonConfig)
        logging.info("Initiate Data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(trainingPipelineConfig)
        logging.info("Initiating data transformation")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("Initiating data transformation")
        print(data_transformation_artifact)
        logging.info("Data Transformation done")

        logging.info("Model Training sstared")
        model_trainer_config=ModelTrainerConfig(trainingPipelineConfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")
    except Exception as e:
        raise NetworkSecuritySystem(e,sys)
    
    ##The code is working proper and we will be deleting artifacts folder and get it later