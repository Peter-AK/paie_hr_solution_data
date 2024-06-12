import pandas as pd
from pandas import DataFrame

from q1 import avg_age_by_dept
from q2 import avg_salary
from q3 import correlation_matrix

# import data set form excel file and fix white spaces
data_set: DataFrame = pd.read_excel("./raw_data/data-test.xlsx")
data_set.columns = [c.replace(" ", "_") for c in data_set.columns]

##################################
# Q1 -- Average age by department
##################################
avg_age_by_dept(data_set=data_set)


##################################
# Q2 -- Average salary by years of experience
##################################
avg_salary(data_set=data_set)

##################################
# Q3 -- Correlation between age and salary
##################################
correlation_matrix(data_set=data_set)
