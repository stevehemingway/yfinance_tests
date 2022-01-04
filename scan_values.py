import yfinance as yf
import pandas as pd
from datetime import datetime
import csv
import math


import quandl
NASDAQ_API_KEY = "mMdxxnhaxfXQ-UqNCyZ_"

quandl.ApiConfig.api_key = NASDAQ_API_KEY

def explore_api(symbol):
    msft = yf.Ticker(symbol)

    # get stock info
    # msft.info

    # msft_var = json.loads(msft.info)

    print(msft.info['shortName'])   
    # show news

    # print(msft.news)

    for i in msft.news:
        print(i['title'])

    return True

# rdr = csv.reader("quotes.csv")

eo_year = datetime.strptime("2020-12-31", "%Y-%m-%d")

def scan_portfolio(portfolio_to_use, max_stocks):
    with open(portfolio_to_use, newline = '') as csvfile:
        rows = csv.DictReader(csvfile)
        rowcount = max_stocks
        for row in rows:
            rowcount -= 1

    #        explore_api(row['Symbol'])
    #        print(row['Symbol'])
            stock = yf.Ticker(row['Symbol'])
            print("{}".format(stock.info['shortName']))
            # print(stock.get_balance_sheet())
            # print(stock.get_balance_sheet().dtypes  )
            bs = stock.get_balance_sheet()
    #        income_statement = stock.get_income_statement()
            cashflow = stock.cashflow
    #        print(bs[eo_year])
    #        print(bs.Series.keys())
            # ['Intangible Assets'])
            headings = cashflow.columns.values
            last_year = headings[0]
            l_y_date = pd.to_datetime(str(last_year))
            # print("date: {}".format(l_y_date.date()))
            # print(cashflow[last_year])
            try:
                buybacks = cashflow[last_year]['Repurchase Of Stock']
                opcash = cashflow[last_year]['Total Cash From Operating Activities']
            except:
                continue
            if not math.isnan(buybacks):
                # print("Stock repurch.: {}".format(buybacks))
                print("buybacks ${:,},/free float ${:,}: {:.2%}".format(buybacks/opcash))
            else:
                continue

            if rowcount <= 0:
                break

def main_yahoo(port):
    scan_portfolio(port, 9999)
    return

# main_yahoo("long_ideas.csv")

def getSingleStock(exchange, symbol, from_date, till_date):    
    repeat_times = 3
    message = ""
    for _ in range(repeat_times): 
        try:
            data = quandl.get(exchange+'/'+symbol, start_date=from_date, end_date=till_date)
            data.index = pd.to_datetime(data.index)
            return data, ""
        except Exception as e:
            message = ", fetch exception: " + str(e)
            continue   
        else:
            time.sleep(0.1)
    return '', message 

#def main_quandl():
#    data = quandl.get("EIA/PET_RWTC_D")
#    print(data)

# main_quandl()

# print("finished")

# data = getSingleStock('EIA', 'PET_RWTC_D', '2021-01-01', '2021-12-31')

#data = getSingleStock('WIKI', 'IBM', '2021-01-01', '2021-12-31')

# print(data)

table_data = quandl.get_table('ZACKS/FC', ticker='AAPL')

for i in table_data.columns:
    print(i)
    
