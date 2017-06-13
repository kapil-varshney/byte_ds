#!/usr/bin/env python3

# Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import pandas as pd

url = 'http://www.nasdaq.com/symbol/aapl/financials?query=income-statement&data=quarterly'

# income-statement: Company, Quarter, Quarter Ending, Total Revenue, Gross Profit, Net Income
# balance-sheet: Total Assets, Total Liabilities, Total Equity
# cash-flow: Net Cash Flow

df = pd.DataFrame(columns = ['Company', 'Quarter', 'Quarter_Ending', 'Total_Revenue', 'Gross_Profit','Net_Income', 'Total_Assets','Total_Liabilities', 'Total_Equity', 'Total_Cash_Flow'],
                  index=range(20))
#print(df)

symbols = ['aapl','amzn', 'fb', 'ibm', 'msft']

# Launch Firefox and navigate to the url
driver = webdriver.Firefox()
driver.get(url)
#driver.quit()

# /html/body/div/div[1]/div[9]/form/div[4]/div[1]/table/thead/tr[1]/th[1]
quarter = driver.find_elements_by_xpath('/html/body/div/div[1]/div[9]/form/div[4]/div[1]/table/thead/tr[1]')
quarter_ending = driver.find_element_by_xpath('/html/body/div/div[1]/div[9]/form/div[4]/div[1]/table/thead/tr[2]')
total_revenue = driver.find_element_by_xpath('/html/body/div/div[1]/div[9]/form/div[4]/div[1]/table/tbody/tr[1]')
gross_profit = driver.find_element_by_xpath('/html/body/div/div[1]/div[9]/form/div[4]/div[1]/table/tbody/tr[3]')
net_income = driver.find_element_by_xpath('/html/body/div/div[1]/div[9]/form/div[4]/div[1]/table/tbody/tr[18]')
print(type(quarter))

blah = quarter[0].text
print(blah)

"""
#print(list(quarter.text))


print(quarter_ending.text)
print(total_revenue.text)
print(gross_profit.text)
print(net_income.text)


url_form = 'http://www.nasdaq.com/symbol/aapl/financials?query={}&data=quarterly'
bs_url = url_form.format("balance-sheet")

driver.get(bs_url)
total_assets = driver.find_element_by_xpath("/html/body/div/div[1]/div[9]/form/div[4]/div[1]/table/tbody/tr[15]")
total_liabilities = driver.find_element_by_xpath("/html/body/div/div[1]/div[9]/form/div[4]/div[1]/table/tbody/tr[26]")
total_equity = driver.find_element_by_xpath("/html/body/div/div[1]/div[9]/form/div[4]/div[1]/table/tbody/tr[33]")

print(total_assets.text)
print(total_equity.text)
print(total_liabilities.text)

cash_flow_url = url_form.format("cash-flow")
driver.get(cash_flow_url)
net_clash_flow = driver.find_element_by_xpath("/html/body/div/div[1]/div[9]/form/div[4]/div[1]/table/tbody/tr[22]")

print(net_clash_flow.text)

"""