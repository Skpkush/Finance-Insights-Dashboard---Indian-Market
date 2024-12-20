# Finance-Insights-Dashboard---Indian-Market


### Finance Insights Dashboard - Indian Market

This project provides an interactive dashboard to analyze the stock performance, trends, and key financial insights of Nifty 50 stocks in the Indian market using **Streamlit** and **Yahoo Finance API**.

## Features

- **Stock Performance Analysis**: Visualize stock price trends over a selected period.
- **Key Financial Metrics**: Display important financial metrics such as market capitalization, P/E ratio, revenue, and more.
- **CAPM (Capital Asset Pricing Model)**: Calculate stock returns using CAPM, incorporating the risk-free rate and market portfolio return.
- **Beta and Alpha Calculation**: Calculate and display the Beta and Alpha values for selected stocks.
- **Stock Comparison**: Compare selected stocks' price performance and their normalized values.
- **Data Fetching**: Get historical stock data, including the closing prices and other key metrics.
- **Interactive Visualization**: Use **Plotly** to create interactive charts for better insights.

## Libraries Used

- `Streamlit`: For building the interactive web dashboard.
- `yfinance`: For downloading stock market data.
- `pandas`: For data manipulation.
- `plotly`: For creating interactive plots.
- `datetime`: For handling date and time functionality.

## Features in Detail

### 1. Stock Performance Analysis
You can select any of the Nifty 50 stocks and specify a date range to fetch historical stock data, including Open, High, Low, Close, and Volume for each trading day. The data is visualized for analysis.

### 2. Key Financial Metrics
The dashboard displays a variety of financial metrics related to the selected stock, including:
- **Current Price**
- **52-Week High/Low**
- **Market Cap**
- **Volume**
- **Book Value**
- Additional metrics like Earnings Per Share (EPS), Return on Equity (ROE), Debt-to-Equity Ratio, Operating Margins, and Free Cash Flow (FCF).

### 3. CAPM Analysis
Using the CAPM formula, you can calculate the expected return for a stock based on its Beta and the market's return. The app provides an easy interface to input data and see the results instantly.

### 4. Beta and Alpha Calculation
The app calculates and displays the Beta and Alpha values of selected stocks. Beta indicates the stock's volatility in relation to the market, while Alpha shows the stock's performance relative to the expected return from CAPM.

### 5. Data Fetching
You can fetch stock data for any ticker from the Nifty 50 list. The dashboard fetches historical stock prices, allowing you to explore stock performance over various intervals, such as daily, weekly, or monthly.

### 6. Interactive Visualization
Charts are created using **Plotly**, making the data interactive. Users can hover over data points, zoom in on specific areas, and compare stock prices over time.

## Example Workflow

1. **Select Stock**: Choose a stock from the Nifty 50 list.
2. **Set Date Range**: Choose the start and end dates for the analysis.
3. **View Key Metrics**: Analyze the key metrics and company overview.
4. **Financial Insights**: View financial metrics like revenue, EPS, ROE, and more.
5. **Stock Comparison**: Compare stock performance with normalized charts.
6. **CAPM**: Calculate expected returns using the CAPM model.
7. **Beta/Alpha**: View the Beta and Alpha values for stock performance comparison.

## Example Output

- **Stock Performance Chart**: Displays price trends for selected stocks.
- **Normalized Stock Performance Chart**: Shows stocks after normalization for easier comparison.
- **Beta and Alpha Values**: A table showing the calculated Beta and Alpha for the selected stocks.
- **CAPM Returns**: A table showing the expected return for each stock based on CAPM.
