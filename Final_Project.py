import yfinance as yf
import requests
import pandas as pd
import plotly.graph_objects as go

def make_graph(stock_data, revenue_data, stock_title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.Date, y=stock_data.Close, name="Stock Price"))
    fig.add_trace(go.Scatter(x=revenue_data.Date, y=revenue_data.Revenue, name="Revenue", yaxis="y2"))
    fig.update_layout(
        title=stock_title,
        xaxis=dict(title="Date"),
        yaxis=dict(title="Stock Price"),
        yaxis2=dict(title="Revenue", overlaying="y", side="right")
    )
    fig.show()

tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print("Tesla Stock Data (first 5 rows):")
print(tesla_data.head())

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text
tesla_revenue = pd.read_html(html_data)[1]
tesla_revenue.columns = ["Date", "Revenue"]
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(",|\$", "", regex=True).astype(float)
tesla_revenue.dropna(inplace=True)
print("\nTesla Revenue Data (last 5 rows):")
print(tesla_revenue.tail())

gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
print("\nGameStop Stock Data (first 5 rows):")
print(gme_data.head())

url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data2 = requests.get(url2).text
gme_revenue = pd.read_html(html_data2)[1]
gme_revenue.columns = ["Date", "Revenue"]
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(",|\$", "", regex=True).astype(float)
gme_revenue.dropna(inplace=True)
print("\nGameStop Revenue Data (last 5 rows):")
print(gme_revenue.tail())

make_graph(tesla_data, tesla_revenue, "Tesla Stock Price vs Revenue")
make_graph(gme_data, gme_revenue, "GameStop Stock Price vs Revenue")
