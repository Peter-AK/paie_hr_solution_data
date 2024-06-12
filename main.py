from datetime import datetime

import pandas as pd
from pandas import DataFrame

# import data set form excel file
data_set: DataFrame = pd.read_excel("./raw_data/data-test.xlsx")

##################################
# Q1 -- Average age by department
##################################


##################################
# Q2 -- salaire moyen en fonction du nombre d’années d’expérience
##################################
data_set["today_date"] = datetime.today()
data_set["delta_days_contract_start"] = data_set["today_date"] - data_set["DEBUT_CONTRAT"]
print(data_set)