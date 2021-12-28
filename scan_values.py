import yfinance as yf
import pandas as pd
from datetime import datetime 
import csv

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
                            
with open('quotes.csv', newline = '') as csvfile:
    rows = csv.DictReader(csvfile)
    rowcount = 1
    for row in rows:
#        explore_api(row['Symbol'])
#        print(row['Symbol'])
        stock = yf.Ticker(row['Symbol'])
        print("{}".format(stock.info['shortName']))
        # print(stock.get_balance_sheet())
        # print(stock.get_balance_sheet().dtypes  )
        bs = stock.get_balance_sheet()
#        print(bs[eo_year])
#        print(bs.Series.keys())
        # ['Intangible Assets'])
        headings = bs.columns.values
        last_year = headings[0]
        l_y_date = pd.to_datetime(str(last_year))
        print("date: {}".format(l_y_date.date()))
        print(bs[last_year])
        rowcount -= 1
        if rowcount <= 0:
            exit()
            
            
