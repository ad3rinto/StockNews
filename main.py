from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import requests
from newsapi import NewsApiClient

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
YEST_DAY = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
PREV_DAY = (datetime.now() - timedelta(2)).strftime("%Y-%m-%d")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": os.environ.get("ALPHA_KEY")
}

PARAMS2 = {
    "q": "Tesla Inc",
    "sources": "bbc-news, the-verge",
    "language": "eng"
}
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
r = requests.get(STOCK_ENDPOINT, params=PARAMS)
r.raise_for_status()
prev_day_close = r.json()["Time Series (Daily)"][PREV_DAY]['4. close']
yest_day_close = r.json()["Time Series (Daily)"][YEST_DAY]['4. close']
price_change = float(prev_day_close) - float(yest_day_close)
real_price_change = abs(round(price_change, 2))
print(f"Price change ia ${real_price_change}")

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

# TODO 2. - Get the day before yesterday's closing stock price

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_change = ((float(prev_day_close) - float(yest_day_close)) / float(prev_day_close)) * 100
final_percent_change = round(percent_change, 2)
print(f"Change is {final_percent_change}%")
# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if final_percent_change < 5:
    newsapi = NewsApiClient(api_key=os.environ.get("NEWS_KEY"))
    top_headlines = newsapi.get_top_headlines(q="binance", sources="bbc-news,the-verge"
                                              , language="en")
    list_of_articles = (top_headlines["articles"])
    for article in list_of_articles:
        print(article["title"], article['url'])
else:
    print("No news here")
## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
