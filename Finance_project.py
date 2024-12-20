import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

# Nifty 50 Stock List (as an example)
nifty_50_stocks = [
    'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'ICICIBANK.NS', 'HUL.NS', 'KOTAKBANK.NS',
    'ITC.NS', 'LT.NS', 'SBIN.NS', 'BAJFINANCE.NS', 'MARUTI.NS', 'HDFC.NS', 'M&M.NS', 'AXISBANK.NS',
    'ASIANPAINT.NS', 'TATAMOTORS.NS', 'WIPRO.NS', 'SUNPHARMA.NS', 'NTPC.NS', 'ONGC.NS', 'BHARTIARTL.NS',
    'ULTRACEMCO.NS', 'DIVISLAB.NS', 'POWERGRID.NS', 'ADANIGREEN.NS', 'DRREDDY.NS', 'TATASTEEL.NS',
    'INDUSINDBK.NS', 'BAJAJ-AUTO.NS', 'COALINDIA.NS', 'IOC.NS', 'UPL.NS', 'GRASIM.NS',
    'HEROMOTOCO.NS', 'CIPLA.NS', 'BHEL.NS', 'INDIAMART.NS', 'EICHERMOT.NS', 'SHREECEM.NS', 'MOTHERSON.NS',
    'TECHM.NS', 'APOLLOHOSP.NS', 'BHARATFORG.NS', 'DLF.NS', 'GAIL.NS', 'HDFCLIFE.NS', 'MINDTREE.NS',
    'TITAN.NS', 'TATACONSUM.NS', 'SBILIFE.NS', 'MPHASIS.NS', 'POLYCAB.NS', 'LICHSGFIN.NS'
]

# Title and Description
st.title("Finance Insights Dashboard - Indian Market")
st.write("Analyze stock performance, trends, insights, and news for Nifty 50 stocks.")

# User Inputs in Main Part
col1, col2 = st.columns(2)
with col1:
    ticker = st.selectbox("Select Stock from Nifty 50", nifty_50_stocks)
    interval = st.selectbox("Select Data Interval:", options=["1d", "1wk", "1mo"], index=0)
with col2:
    start_date = st.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
    end_date = st.date_input("End Date", value=pd.to_datetime(datetime.now()))

# Fetch Data
if st.button("Fetch Data"):
    try:
        # Fetch historical stock data
        data = yf.download(ticker, start=start_date, end=end_date, interval=interval)

        if data.empty:
            st.error(f"No data found for ticker: {ticker}. Please check the ticker symbol.")
        else:
            # Display Key Metrics
            ticker_info = yf.Ticker(ticker).info
            st.subheader(f"Key Metrics for {ticker.upper()}")
            col1, col2, col3 = st.columns(3)

            # Safely format values (only if they are numeric)
            def safe_format(values):
                try:
                    return f"₹{float(values):,.2f}"
                except (ValueError, TypeError):
                    return values


            col1.metric("Current Price", safe_format(ticker_info.get('currentPrice', 'N/A')))
            col3.metric("Market Cap", safe_format(ticker_info.get('marketCap', 'N/A')))
            col1.metric("52-Week High", safe_format(ticker_info.get('fiftyTwoWeekHigh', 'N/A')))
            col2.metric("52-Week Low", safe_format(ticker_info.get('fiftyTwoWeekLow', 'N/A')))
            col3.metric("Volume", safe_format(ticker_info.get('volume', 'N/A')))
            col2.metric("Book Value", safe_format(ticker_info.get('bookValue', 'N/A')))
            # Enhanced Performance Summary
            st.subheader(f"Company Overview - {ticker.upper()}")
            st.write(f"Company: **{ticker_info.get('shortName', 'N/A')}**")
            st.write(f"Sector: **{ticker_info.get('sector', 'N/A')}**")
            st.write(f"Industry: **{ticker_info.get('industry', 'N/A')}**")
            st.write(f"Full-Time Employees: **{ticker_info.get('fullTimeEmployees', 'N/A')}**")
            st.write(f"**Business Segments:** {ticker_info.get('sector','N/A')}")
            st.write(f"**Market Capitalization:** {ticker_info.get('marketCap', 'N/A')}")
            st.write(f"**Core Business Areas:** {ticker_info.get('sector', 'N/A')}")
            st.write(f"**Global Presence:** {ticker_info.get('country', 'N/A')} countries")

            # Additional Financial Insights
            # Display Financial Insights in a table
            st.subheader("Financial Metrics")

            # Create a list of tuples for the financial metrics
            financial_metrics = [
                ("Revenue", safe_format(ticker_info.get('totalRevenue', 'N/A'))),
                ("Net Income", safe_format(ticker_info.get('netIncomeToCommon', 'N/A'))),
                ("Earnings Per Share (EPS)", ticker_info.get('trailingEps', 'N/A')),
                ("Return on Equity (ROE)", ticker_info.get('returnOnEquity', 'N/A')),
                ("Debt-to-Equity Ratio", ticker_info.get('debtToEquity', 'N/A')),
                ("Current Ratio", ticker_info.get('currentRatio', 'N/A')),
                ("Quick Ratio", ticker_info.get('quickRatio', 'N/A')),
                ("Operating Margin", ticker_info.get('operatingMargins', 'N/A')),
                ("Gross Margin", ticker_info.get('grossMargins', 'N/A')),
                ("Free Cash Flow (FCF)", safe_format(ticker_info.get('freeCashflow', 'N/A')))
            ]

            # Display the financial metrics in a table
            st.table(financial_metrics)

            # Recent News
            st.subheader("Recent News")
            st.write("Fetching recent news is currently not implemented but can be integrated using a news API.")

            # Analyst Ratings
            st.subheader("Outlook/Analyst Ratings")
            st.write(f"Analyst Recommendations: **{ticker_info.get('recommendationKey', 'N/A')}**")

    except Exception as e:
        st.error(f"Error fetching data. Please check the stock ticker and try again. Details: {str(e)}")

# importing libraries
import streamlit as st
import datetime
import yfinance as yf
import pandas as pd
import capm_functions

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
        ['RELIANCE'],
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
