# importing libraries
import streamlit as st
import datetime
import yfinance as yf
import pandas as pd
import capm_functions

# setting page config
st.set_page_config(
    page_title="CAPM",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)

st.title('Capital Asset Pricing Model (Indian Market) 📈')

# getting input from user
col1, col2 = st.columns([1, 1])
with col1:
    stocks_list = st.multiselect(
        "Choose 4 Stocks",
        ('RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'ICICIBANK', 'SBIN', 'ADANIGREEN',
    'BHARTIARTL', 'ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO',
    'BAJAJFINSV', 'BAJFINANCE', 'BPCL', 'BRITANNIA', 'CIPLA', 'COALINDIA',
    'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFC',
    'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'ITC', 'JSWSTEEL', 'KOTAKBANK',
    'LT', 'M&M', 'MARUTI', 'NESTLEIND', 'NTPC', 'ONGC', 'POWERGRID', 'SBILIFE',
    'SUNPHARMA', 'TATACONSUM', 'TATAMOTORS', 'TATASTEEL', 'TECHM', 'TITAN',
    'UPL', 'ULTRACEMCO', 'WIPRO'),
        ['RELIANCE', 'TCS', 'INFY', 'HDFCBANK'],
        key="stock_list",
    )
with col2:
    year = st.number_input("Number of Years", 1, 10)

try:
    # downloading data for NIFTY 50 index
    end = datetime.date.today()
    start = datetime.date(datetime.date.today().year - year, datetime.date.today().month, datetime.date.today().day)
    nifty50 = yf.download('^NSEI', start=start, end=end)
    nifty50 = nifty50[['Close']].reset_index()
    nifty50.columns = ['Date', 'nifty50']

    # downloading data for the selected stocks
    stocks_df = pd.DataFrame()
    for stock in stocks_list:
        data = yf.download(stock + ".NS", start=start, end=end)  # Use ".NS" suffix for Indian stocks
        stocks_df[f'{stock}'] = data['Close']
    stocks_df.reset_index(inplace=True)
    stocks_df.columns = ['Date'] + stocks_list
    stocks_df['Date'] = stocks_df['Date'].astype('datetime64[ns]')
    stocks_df = pd.merge(stocks_df, nifty50, on='Date', how='inner')

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown('### Dataframe head')
        st.dataframe(stocks_df.head(), use_container_width=True)
    with col2:
        st.markdown('### Dataframe tail')
        st.dataframe(stocks_df.tail(), use_container_width=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown('### Price of all the Stocks')
        st.plotly_chart(capm_functions.interactive_plot(stocks_df))

    with col2:
        st.markdown('### Price of all the Stocks (After Normalizing)')
        st.plotly_chart(capm_functions.interactive_plot(capm_functions.normalize(stocks_df)))

    # calculating daily return
    stocks_daily_return = capm_functions.daily_return(stocks_df)

    beta = {}
    alpha = {}

    for i in stocks_daily_return.columns:
        # Ignoring the date and NIFTY 50 Columns
        if i != 'Date' and i != 'nifty50':
            # calculate beta and alpha for all stocks
            b, a = capm_functions.calculate_beta(stocks_daily_return, i)
            beta[i] = b
            alpha[i] = a

    col1, col2 = st.columns([1, 1])

    beta_df = pd.DataFrame(columns=['Stock', 'Beta Value'])
    beta_df['Stock'] = beta.keys()
    beta_df['Beta Value'] = [str(round(i, 2)) for i in beta.values()]

    with col1:
        st.markdown('### Calculated Beta Value ')
        st.dataframe(beta_df, use_container_width=True)

    # Calculate return for any security using CAPM
    rf = 0  # risk-free rate of return
    rm = stocks_daily_return['nifty50'].mean() * 252  # market portfolio return
    return_df = pd.DataFrame()
    stock_list = []
    return_value = []
    for stock, value in beta.items():
        stock_list.append(stock)
        # calculate return
        return_value.append(str(round(rf + (value * (rm - rf)), 2)))
    return_df['Stock'] = stock_list
    return_df['Return Value'] = return_value

    with col2:
        st.markdown('### Calculated Return using CAPM ')
        st.dataframe(return_df, use_container_width=True)

except Exception as e:
    st.write(f"An error occurred: {e}")
