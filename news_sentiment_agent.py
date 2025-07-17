from newsapi_tool import response
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.tools import Tool,tool
import trafilatura 
import goose3 
from goose3 import Goose
from dotenv import load_dotenv
from yfinance_tool import name

load_dotenv()

company_name ="ONGC"

url_link=[]

# 🖨️ Display Top Results
print(f"🔍 News results for: {company_name}\n")
for i, article in enumerate(response['articles'], 1):
    print(f"{i}. {article['title']}")
    print(f"   🗞️ {article['source']['name']} | 📅 {article['publishedAt']}")
    print(f"   🔗 {article['url']}\n")
    url_link.append(article['url'])

print("Extracted URLs:")
print(url_link)

def extract_article_info(url):
    article = trafilatura.fetch_url(url)
    extracted=trafilatura.extract(article)
    return extracted

summary=[]
sentiment=[]

for i in url_link:
    info = extract_article_info(i)
    summary.append(info) 

def summarizer(summary_main):
    llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)

    messages = [
        {"role": "system", "content":"You are an expert news sentiment analyst. You will be given information and you have to return whether it is a positive or negative news to the company.Give it only in 1 line.Only classify whether it is a positive or negative sentiment for the company.)"},
        {"role": "user", "content":f"Context:{summary_main},Company:{name}"}
    ]

    response = llm.invoke(messages)
    print("Final response:",response.content)
    sentiment.append(response.content)
    return sentiment

for i in summary:
    summarizer(i)
print("Sentimental Analysis:")
print(len(sentiment))
print(sentiment)
