# import json
import yfinance as yf


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

for 
explore_api("MSFT")


def other_stuff():
        
    # get historical market data
    hist = msft.history(period="max")

    # show actions (dividends, splits)
    msft.actions

    # show dividends
    msft.dividends

    # show splits
    msft.splits

    # show financials
    msft.financials
    msft.quarterly_financials

    # show major holders
    msft.major_holders

    # show institutional holders
    msft.institutional_holders

    # show balance sheet
    msft.balance_sheet
    msft.quarterly_balance_sheet

    # show cashflow
    msft.cashflow
    msft.quarterly_cashflow

    # show earnings
    msft.earnings
    msft.quarterly_earnings

    # show sustainability
    msft.sustainability

    # show analysts recommendations
    msft.recommendations

    # show next event (earnings, etc)
    msft.calendar

    # show ISIN code - *experimental*
    # ISIN = International Securities Identification Number
    msft.isin

    # show options expirations
    msft.options

    # get option chain for specific expiration
    opt = msft.option_chain('2022-01-21')
    # data available via: opt.calls, opt.puts

