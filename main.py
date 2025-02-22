import os
import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecuritySystem
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
##To know what to import like above just check __init__ of that file and see what it is aslking/demanding to be executed

if __name__=="__main__":
    try:
        trainingPipelineConfig=TrainingPipelineConfig()
        dataIngestionConfig=DataIngestionConfig(trainingPipelineConfig)
        dataIngestion=DataIngestion(dataIngestionConfig)
        logging.info("Initiate the data ingestion")
        data_ingestion_artifact=dataIngestion.initate_data_ingestion()
        print(data_ingestion_artifact)
    except Exception as e:
        raise NetworkSecuritySystem(e,sys)
    
    ##The code is working proper and we will be deleting artifacts folder and get it later