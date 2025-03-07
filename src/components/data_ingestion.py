import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataClassconfig:
    train_test_path: str = os.path.join('artifacts','train_test_data.csv')
    test_path: str = os.path.join('artifacts','test_data.csv')
    raw_path: str = os.path.join('artifacts','raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataClassconfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion has started")
        try:
            df = pd.read_csv("notebook/stud.csv")
            logging.info("Reading the data")
            os.makedirs(os.path.dirname(self.ingestion_config.train_test_path),exist_ok=True) 
            df.to_csv(self.ingestion_config.raw_path,index=False,header=True)
            logging.info("Raw data has been saved")

            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)   
            logging.info("Train test split is initiated")
            train_set.to_csv(self.ingestion_config.train_test_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_path,index=False,header=True)
            logging.info("Data ingestion is completed")

            return(
                self.ingestion_config.test_path,
                self.ingestion_config.train_test_path
            )

        except Exception as e:
            raise CustomException(e,sys)    

# if __name__ == "__main__":
#     obj = DataIngestion()
#     obj.initiate_data_ingestion()


