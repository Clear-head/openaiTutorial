import streamlit as st

from stock_search import stock_search
from stock_info import StockInfo
from report_service import investment_report


class SearchResult:
    def __init__(self, item):
        self.item = item


    @property
    def symbol(self):
        return self.item["Symbol"]
    @property
    def name(self):
        return self.item["Name"]

    def __str__(self):
        return f"{self.symbol} : {self.name}"

st.title("Stock Search App")
search_qry = st.text_input("Search", 'Apple')
search_results = [SearchResult(hit) for hit in stock_search(search_qry)['hits']]

selected_search_result = st.selectbox("Stock Search Results", search_results)

stock = StockInfo(selected_search_result.symbol)
st.write(stock.get_basic_info())
st.write(stock.get_financial_stat())
b = st.button("create report")


if b:
    st.header("Stock Report")
    st.write(investment_report(selected_search_result.symbol, selected_search_result.name, stock))