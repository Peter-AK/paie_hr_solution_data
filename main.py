import pandas as pd
from pandas import DataFrame

from q2 import avg_salary

# import data set form excel file and fix white spaces
data_set: DataFrame = pd.read_excel("./raw_data/data-test.xlsx")
data_set.columns = [c.replace(' ', '_') for c in data_set.columns]

##################################
# Q1 -- Average age by department
##################################

##################################
# Q2 -- Average salary by years of experience
##################################
avg_salary(data_set=data_set)
