# importing libraries
import streamlit as st
import datetime
import pandas_datareader.data as web
import yfinance as yf
import pandas as pd
import capm_functions
import plotly.express as px

# setting page config
st.set_page_config(
    page_title="Beta Caculation",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)

st.title('Calculate Beta and Return for Individual Stock (Indian Market)')

# getting input from user
col1, col2 = st.columns([1, 1])
with col1:
    stock = st.selectbox("Choose a stock", ('RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'ICICIBANK', 'SBIN', 'ADANIGREEN',
    'BHARTIARTL', 'ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO',
    'BAJAJFINSV', 'BAJFINANCE', 'BPCL', 'BRITANNIA', 'CIPLA', 'COALINDIA',
    'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFC',
    'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'ITC', 'JSWSTEEL', 'KOTAKBANK',
    'LT', 'M&M', 'MARUTI', 'NESTLEIND', 'NTPC', 'ONGC', 'POWERGRID', 'SBILIFE',
    'SUNPHARMA', 'TATACONSUM', 'TATAMOTORS', 'TATASTEEL', 'TECHM', 'TITAN',
    'UPL', 'ULTRACEMCO', 'WIPRO'))
with col2:
    year = st.number_input("Number of Years", 1, 10)

# downloading data for NIFTY50
end = datetime.date.today()
start = datetime.date(datetime.date.today().year - year, datetime.date.today().month, datetime.date.today().day)
nifty50 = yf.download('^NSEI', start=start, end=end)
nifty50 = nifty50[['Close']]
nifty50.columns = ['nifty50']
nifty50.reset_index(inplace=True)

# downloading data for the stock
stocks_df = yf.download(stock + ".NS", period=f'{year}y')  # Use .NS suffix for Indian stocks
stocks_df = stocks_df[['Close']]
stocks_df.columns = [f'{stock}']
stocks_df.reset_index(inplace=True)
nifty50.columns = ['Date', 'nifty50']
stocks_df['Date'] = stocks_df['Date'].astype('datetime64[ns]')
stocks_df = pd.merge(stocks_df, nifty50, on='Date', how='inner')

# calculating daily return
stocks_daily_return = capm_functions.daily_return(stocks_df)
rm = stocks_daily_return['nifty50'].mean() * 252

# calculate beta and alpha
beta, alpha = capm_functions.calculate_beta(stocks_daily_return, stock)

# risk-free rate of return
rf = 0

# market portfolio return
rm = stocks_daily_return['nifty50'].mean() * 252

# calculate return
return_value = round(rf + (beta * (rm - rf)), 2)

# showing results
st.markdown(f'### Beta : {beta}')
st.markdown(f'### Return  : {return_value}')
fig = px.scatter(stocks_daily_return, x='nifty50', y=stock, title=stock)
fig.add_scatter(x=stocks_daily_return['nifty50'], y=beta * stocks_daily_return['nifty50'] + alpha, line=dict(color="crimson"))
st.plotly_chart(fig, use_container_width=True)
