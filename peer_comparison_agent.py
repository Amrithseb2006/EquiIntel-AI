from peer_comparison_tool import rows
from langchain_community.chat_models import ChatOpenAI
from yfinance_tool import name
from dotenv import load_dotenv
load_dotenv()

from fin_terms import financial_terms
peer_list=[]
llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)
for i in range(5):
    peer_list.append(rows[i])

messages =[
    {"role":"system","content":"You are an financial Expert. You will be given a company along with its peers. You have to compare the metrics and you can give a suggestion of why other stocks maybe better or worse and for what type of investors.Evaluate according to the definiton of the financial terms provided.The metrics are given in the following order symbol, longName, marketCap, currentPrice ,beta , trailingPE,trailingAnnualDividendYield,bookValue,priceToBook,earningsQuarterlyGrowth,trailingEps,returnOnEquity"},
    {"role":"user","content":f"Here is the company name {name} and its peers: {peer_list}. Financial metrics are {financial_terms}"}
]

response = llm.invoke(messages)
print(response.content)
