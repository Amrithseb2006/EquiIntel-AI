from newsapi import NewsApiClient
from datetime import datetime, timedelta

# 🔐 Replace with your own API Key from newsapi.org
NEWS_API_KEY = '39c018b45b444799a5c30a91df1d87ae'

# Initialize
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

# Parameters
company_name = "ONGC"
query = f'"{company_name}"'
from_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')  # past 7 days

# 📰 Fetch News
response = newsapi.get_everything(
    q=query,
    from_param=from_date,
    language='en',
    sort_by='publishedAt',
    page_size=5,
)

# 🖨️ Display Top Results
print(f"🔍 News results for: {company_name}\n")
for i, article in enumerate(response['articles'], 1):
    print(f"{i}. {article['title']}")
    print(f"   🗞️ {article['source']['name']} | 📅 {article['publishedAt']}")
    print(f"   🔗 {article['url']}\n")
