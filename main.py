import datetime

import requests
from datetime import datetime as dt


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK = "PMYFP4RPQSDEJSR9"
API_KEY_NEWS = "89ca6f655429407eb00c9ac6e593e0cd"


s = requests.get(url=f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={API_KEY_STOCK}')
data_stocks = s.json()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
today = dt.today()
yesterday = str((today - datetime.timedelta(days=2)).date())
day_before = str((today - datetime.timedelta(days=3)).date())
today = today.date()


day_before_closing_price = float(data_stocks["Time Series (Daily)"][day_before]["4. close"])
yesterday_closing_price = float(data_stocks["Time Series (Daily)"][yesterday]["4. close"])
difference = abs(yesterday_closing_price-day_before_closing_price)
if (difference/yesterday_closing_price)*100 > 5:
    news = requests.get(url=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={today}"
                            f"&sortBy=publishedAt&apiKey={API_KEY_NEWS}")
    data_news = news.json()
    for n in data_news["articles"][0:1]:
        source = n["source"]["name"]
        print(f"Source: {source}")
        author = n["author"]
        print(f"Author: {author}")
        title = n["title"]
        print(f"Title: {title}")
        description = n["description"]
        print(f"Description: {description}")
        content = n["content"]
        print(f"Content: {content}")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# DONE




## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

