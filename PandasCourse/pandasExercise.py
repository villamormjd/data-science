import numpy as np
import pandas as pd

from numpy.random import randn


"""
Read Salaries.csv as DataFrame call sal.

sal.info() returns number of colums and number of entry rows
"""
sal = pd.read_csv('../FolderFile/Salaries.csv')

"""
Get the average BasePay and Highest OT Pay
"""
sal['BasePay'].mean()
sal['OvertimePay'].max()

"""
1. Finding JobTitle of specific employee and totalPaybenefits
2. Finding EmployeeName with Highest TotalyPayBenefits
3. Finding Name with Lowest TPB
"""
employee = "joseph driscoll".upper()
sal[sal['EmployeeName'] == employee]['JobTitle']
sal[sal['EmployeeName'] == employee]['TotalPayBenefits']

highest_benefit = sal['TotalPayBenefits'].max()
sal[sal['TotalPayBenefits'] == highest_benefit]['EmployeeName']

# sal.iloc[sal['TotalPayBenefits'].argmin()]

"""
Getting Average basePay of All Employees per year
 Use groupby() method
 
 nunique() to get the number of JobTitles
"""
sal.groupby('Year').mean()['BasePay']
sal['JobTitle'].nunique()

"""
Get the 5 most common Jobs
"""
top = sal['JobTitle'].value_counts().head(5)

"""
Figure out how many (SUM) job title were represented by only one person in 2013
"""

job_count = sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)

"""
Finding how many people with word Chief in Job Title
"""


def chief_string(string):
    if 'chief' in string.lower():
        return True

    return False


total = sum(sal['JobTitle'].apply(lambda x: chief_string(x)))

"""
Correlation

corr() method returns correlation between columns
"""

sal['title_len'] = sal['JobTitle'].apply(len)
corr = sal[['TotalPayBenefits', 'title_len']].corr()

