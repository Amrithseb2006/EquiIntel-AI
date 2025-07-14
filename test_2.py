from yfinance_tool import name, summary, ind, beta, pe, div_yield, book_value, pb, earnings_q, eps, y_change, current_price, roe, currency, exchange,market_cap
from fin_terms import financial_terms
from langchain_community.chat_models import ChatOpenAI

from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
#os.environ["OPENAI_API_KEY"] = openai.api_key

# Dictionary of financial definitions
fin_term_dict = financial_terms()

# Combine the data into a dictionary
company_data = {
    "Company Name": name,
    "Summary": summary,
    "Industry": ind,
    "Beta": beta,
    "P/E Ratio": pe,
    "Dividend Yield (%)": div_yield,
    "Book Value": book_value,
    "P/B Ratio": pb,
    "Quarterly Earnings": earnings_q,
    "EPS": eps,
    "52W Change (%)": y_change,
    "Current Price": current_price,
    "ROE (%)": roe,
    "Currency": currency,
    "Exchange": exchange
}

# Optional: Pretty print company data
for key, value in company_data.items():
    print(f"\n{key}: {value}")

# LLM Generator function
def generator():
    llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

    system_message = {
        "role": "system",
        "content": (
            "You are a financial expert. Based on the given financial metrics and definitions, "
            "generate a comprehensive but concise financial summary. "
            "Here are the financial terms with their definitions:\n"
            f"{fin_term_dict}"
        )
    }

    # Format company data into a readable string
    user_message = {
        "role": "user",
        "content": "\n".join([f"{k}: {v}" for k, v in company_data.items()])
    }

    response = llm.invoke([system_message, user_message])
    return response.content

# Get the answer
answer = generator()
print("\n📊 Financial Summary:\n")
print(answer)
