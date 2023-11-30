import pandas as pd
import yfinance as yf
import streamlit as st

st.write("""
         ## Simple stock price app

         Shown are the stock **closing** price and **volume** of on Apple!
         """)

tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = '1d', start = '2013-11-30', end = '2023-11-30')

#st.line_chart(tickerDf.Close)
#st.line_chart(tickerDf.Volume)
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
