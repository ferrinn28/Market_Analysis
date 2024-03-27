import yfinance as yf
from pprint import pprint
from .utills import get_last_day_of_month

def main():
    ticker_name = "TLKM.JK"
    ticker = yf.Ticker(ticker_name)

    quartal_income_stmt = ticker.quarterly_income_stmt

    print(dir(ticker))

    for data in quartal_income_stmt.columns:
        print(type(data))
        data_date = data.date()

        print(data_date, type(data_date))
        print(dir(data_date))
        print(data_date.day, type(data_date.day))
        print("\n")