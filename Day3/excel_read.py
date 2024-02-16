""" reading of excel file and analysis"""
import pandas as pd

pd.set_option('display.max_columns', None)


f1=pd.read_excel('./externalFiles/emp1.xlsx')
#print(f1)

"""
#data Analysis to chk whether the eid are unique
if f1['EEID'].is_unique:
    print("eids are UNIQUE")
else:
    print("eids are NOT UNIQUE")
"""
#Full Name : split into fn and ln
f1[['fn', 'ln']]=f1['Full Name'].str.split(' ', expand=True)
#print(f1[['fn', 'ln']])
"""
#create an dictionary and store the fn & ln
dc_en=f1[['fn', 'ln']].to_dict(orient='records')
print(dc_en)
"""

for jt, grp_jt in f1.groupby('Job Title'):
    print("Employees working as: ", jt.upper())
    print(grp_jt['Full Name'], "\n")
