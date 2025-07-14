from newsapi_tool import response
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.tools import Tool,tool
import newspaper3k 
from newspaper import Article

company_name ="ONGC"

url_link=[]

# 🖨️ Display Top Results
print(f"🔍 News results for: {company_name}\n")
for i, article in enumerate(response['articles'], 1):
    print(f"{i}. {article['title']}")
    print(f"   🗞️ {article['source']['name']} | 📅 {article['publishedAt']}")
    print(f"   🔗 {article['url']}\n")
    url_link.append(article['url'])

print(url_link)

def extract_article_info(url):
    article = Article(url)
    article.download()
    article.parse
    return article.text

info = extract_article_info("https://www.opindia.com/2025/07/cci-probes-ultratech-dalmia-for-cement-cartel-in-ongc-tenders/")


