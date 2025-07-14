from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.tools import Tool,tool

from dotenv import load_dotenv
import os 
import openai

from yfinance_tool import name, summary, ind, beta, pe, div_yield, book_value, pb, earnings_q, eps, y_change, current_price, roe, currency, exchange,market_cap
from fin_terms import financial_terms

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

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
    "Exchange": exchange,
    "Market Capitalization": market_cap
}

# Optional: Pretty print company data
for key, value in company_data.items():
    print(f"\n{key}: {value}")

@tool
def finance_summarizer():

    """
    Summarize based on the financial metrics.
    """

    llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)

    system_message = {
        "role" : "system",
        "content" : (
           f"""You are a financial analyst writing investment summaries for retail investors.

            You must:
            - Interpret each financial metric (P/E, EPS, ROE, etc.)
            - Use the definitions provided
            - Avoid generic statements (e.g., "This is a good company.")
            - Write clearly and concisely

            Here are financial definitions:
            {financial_terms}"""

        )
    }

    user_message = {
    "role": "user",
    "content": (
        f"""
        You are provided with key financial metrics for a company.

        Please analyze the financial health and investment attractiveness of the company using the following information. Interpret the numbers meaningfully — do not just list them. Focus on valuation, profitability, market performance, and overall financial strength.

        Here are the metrics:

        {chr(10).join([f"- {key}: {value}" for key, value in company_data.items()])}

        Based on the above data, generate a concise and insightful summary that would help an investor understand the company's current financial position and attractiveness.
        """
        )
    }


    results = llm.invoke([system_message,user_message])
    return results.content


finance_agent = initialize_agent(tools=[Tool(name="RAG Query", func=finance_summarizer,
                description="Answer based on summarized text.")],
                llm=ChatOpenAI(model_name="gpt-4o-mini"),
                agent="zero-shot-react-description",
                verbose=True)

answer = finance_agent.run("Summarize the financial data.")
print(answer)

