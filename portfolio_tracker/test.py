import datetime

from yahoo_fin.stock_info import get_data
from datetime import date

start = date.today()
end = start + datetime.timedelta(1)

tickers = [
    'AAPL', 'ABI.BR', 'AD.AS', 'AGS.BR', 'BABA', 'CRWD',
    'IWDA.AS', 'PRX.AS', 'UCB.BR', 'VUSA.AS', 'WTEJ.DE', 'XCS6.DE'
]

for ticker in tickers:
    data = get_data(ticker, start_date=start, end_date=end)
    print(ticker, ':',  data.iloc[-1].close)
    print('----')
