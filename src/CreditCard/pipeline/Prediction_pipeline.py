import os
import sys
import pandas as pd
from src.CreditCard.logger import logging
from src.CreditCard.utils.utils import load_object
from src.CreditCard.exception import customexception

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            preprocessor_path=os.path.join("Artifacts","preprocessor.pkl")
            model_path=os.path.join("Artifacts","model.pkl")
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            scaled_data=preprocessor.transform(features)
            pred=model.predict(scaled_data)
            return pred

        except Exception as e:
            raise customexception(e,sys)
    
class CustomData:
    def __init__(self,
                 LIMIT_BAL:float,
                 SEX:int,
                 EDUCATION:int,
                 MARRIAGE:int,
                 AGE:int,
                 PAY_SEPT:int,
                 PAY_AUG:int,
                 PAY_JUL:int,
                 PAY_JUN:int,
                 PAY_MAY:float,
                 PAY_APR:int,
                 BILL_AMT_SEPT:float,
                 BILL_AMT_AUG:float,
                 BILL_AMT_JUL:float,
                 BILL_AMT_JUN:float,
                 BILL_AMT_MAY:float,
                 BILL_AMT_APR:float,
                 PAY_AMT_SEPT:float,
                 PAY_AMT_AUG:float,
                 PAY_AMT_JUL:float,
                 PAY_AMT_JUN:float,
                 PAY_AMT_MAY:float,
                 PAY_AMT_APR:float
                
                 ):
        
        self.LIMIT_BAL = LIMIT_BAL
        self.SEX = SEX
        self.EDUCATION = EDUCATION
        self.MARRIAGE = MARRIAGE
        self.AGE = AGE
        self.PAY_SEPT = PAY_SEPT
        self.PAY_AUG = PAY_AUG
        self.PAY_JUL = PAY_JUL
        self.PAY_JUN = PAY_JUN
        self.PAY_MAY = PAY_MAY
        self.PAY_APR = PAY_APR
        self.BILL_AMT_SEPT = BILL_AMT_SEPT
        self.BILL_AMT_AUG=BILL_AMT_AUG
        self.BILL_AMT_JUL = BILL_AMT_JUL
        self.BILL_AMT_JUN = BILL_AMT_JUN
        self.BILL_AMT_MAY = BILL_AMT_MAY
        self.BILL_AMT_APR = BILL_AMT_APR
        self.PAY_AMT_SEPT = PAY_AMT_SEPT
        self.PAY_AMT_AUG = PAY_AMT_AUG
        self.PAY_AMT_JUL = PAY_AMT_JUL
        self.PAY_AMT_JUN = PAY_AMT_JUN
        self.PAY_AMT_MAY = PAY_AMT_MAY
        self.PAY_AMT_APR = PAY_AMT_APR
       


            
                
    def get_data_as_dataframe(self):
            try:
                custom_data_input_dict = {
                    'LIMIT_BAL':[self.LIMIT_BAL],
                    'SEX':[self.SEX],
                    'EDUCATION':[self.EDUCATION],
                    'MARRIAGE':[self.MARRIAGE],
                    'AGE':[self.AGE],
                    'PAY_SEPT':[self.PAY_SEPT],
                    'PAY_AUG':[self.PAY_AUG],
                    'PAY_JUL':[self.PAY_JUL],
                    'PAY_JUN':[self.PAY_JUN],
                    'PAY_MAY':[self.PAY_MAY],
                    'PAY_APR':[self.PAY_APR],
                    'BILL_AMT_SEPT':[self.BILL_AMT_SEPT],
                    'BILL_AMT_AUG':[self.BILL_AMT_AUG],
                    'BILL_AMT_JUL':[self.BILL_AMT_JUL],
                    'BILL_AMT_JUN':[self.BILL_AMT_JUN],
                    'BILL_AMT_MAY':[self.BILL_AMT_MAY],
                    'BILL_AMT_APR':[self.BILL_AMT_APR],
                    'PAY_AMT_SEPT':[self.PAY_AMT_SEPT],
                    'PAY_AMT_AUG':[self.PAY_AMT_AUG],
                    'PAY_AMT_JUL':[self.PAY_AMT_JUL],
                    'PAY_AMT_JUN':[self.PAY_AMT_JUN],
                    'PAY_AMT_MAY':[self.PAY_AMT_MAY],
                    'PAY_AMT_APR':[self.PAY_AMT_APR]
                    

                }
                df = pd.DataFrame(custom_data_input_dict)
                print(df)
                logging.info('Dataframe Gathered')
                return df
            except Exception as e:
                logging.info('Exception Occured in prediction pipeline')
                raise customexception(e,sys)