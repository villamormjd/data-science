import pandas as pd


ecom = pd.read_csv('../FolderFile/Ecommerce Purchases')

"""
Column Names: 
Index(['Address', 'Lot', 'AM or PM', 'Browser Info', 'Company', 'Credit Card',
       'CC Exp Date', 'CC Security Code', 'CC Provider', 'Email', 'Job',
       'IP Address', 'Language', 'Purchase Price'],
      dtype='object')
      
.columns() & .index()
"""
# 1
ave_purchase_price = ecom['Purchase Price'].mean()

# 2
en = ecom[ecom['Language'] == 'en']['Language'].count()

job_lawyer = ecom[ecom['Job'] == 'Lawyer'].count()

am_pm = ecom['AM or PM'].value_counts()

most_common_jobs = ecom['Job'].value_counts().head(5)

lot_purchase_price = ecom[ecom['Lot'] == '90 WT']['Purchase Price']

email_address = ecom[ecom['Credit Card'] == 4926535242672853]['Email']

people = ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count()

exp_date = sum(ecom['CC Exp Date'].apply(lambda exp: exp[3:] == '25'))

"""
get most popular email_providers.
"""
email_providers = ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5)

"""
:returns: records with single digit security code
"""
single_security_code = ecom[ecom['CC Security Code'].apply(lambda x: len(str(x))) == 1]['Credit Card']
