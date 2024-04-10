from scipy.stats import spearmanr
import pandas as pd

df = pd.read_csv('processed_data.csv', on_bad_lines='skip')

 
# calculate Spearman's correlation coefficient and p-value
corr, pval = spearmanr(df['GASUSGE'],df['URBAN'], nan_policy='omit')
 
for column in df:
    print(column)
    corr, pval = spearmanr(df['GASUSGE'],df[column], nan_policy='omit')
    print("Spearman's correlation coefficient:", corr)
    print("p-value:", pval)
# print the result
print("Spearman's correlation coefficient:", corr)
print("p-value:", pval)



