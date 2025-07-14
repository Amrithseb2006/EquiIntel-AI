# 📊 EquiIntel — AI-Powered Stock Report Generator

**EquiIntel** is an AI-powered, multi-agent stock analysis system that autonomously generates detailed, investment-grade reports using real-time financial data, news sentiment, peer comparisons, and visual insights.

---

## 🎯 Objective

To create a modular, intelligent stock report generator that:
- Uses a multi-agent system with LLM-based reasoning
- Fetches live financial metrics, news, and peer data
- Summarizes complex financials in plain language
- Outputs structured PDF or HTML reports

---

## 🧠 Key Features

- 📈 **Live Data Fetching** from Yahoo Finance and NewsAPI
- 🤖 **Multi-Agent Architecture** with LangChain Agents
- 🧾 **LLM-Generated Summaries** of stock performance
- 📰 **News Sentiment Analysis** with tone detection
- 📊 **Peer Comparison** and financial benchmarking
- 🖼️ **Visualizations** (Price trends, P/E vs Industry, etc.)
- 📄 **PDF/HTML Export** for shareable reports
- 📚 **Financial Term Glossary** for easy understanding

---

## 🧩 Architecture Overview

```text
User Input → LeadAgent
            ↳ FinancialDataAgent (yfinance)
            ↳ NewsSentimentAgent (NewsAPI + GPT)
            ↳ PeerComparisonAgent
            ↳ FundamentalAnalysisAgent
            ↳ ChartGeneratorAgent
            ↳ SummaryAgent
                ↓
        Final report → PDF / HTML


## 🔧 Technology Stack

| Layer                  | Tools/Technologies                                        |
|------------------------|-----------------------------------------------------------|
| **Data Fetching**      | `yfinance`, `NewsAPI`, `Yahoo Finance API`                |
| **LLM / Reasoning**    | `OpenAI GPT-4o`, `LangChain`                              |
| **Agent Orchestration**| `LangChain Agents`, `LangGraph` *(optional)*, `CrewAI` *(optional)* |
| **Visualization**      | `matplotlib`, `seaborn`, `plotly`                         |
| **Export**             | `fpdf`, `jinja2`, `pdfkit` *(optional)*                   |
| **RAG (Optional)**     | `LangChain + Pinecone + OCR` *(for transcripts)*          |

---

## 📁 Project Structure

equiintel/
├── agents/
│   ├── lead_agent.py               # Master agent / task planner
│   ├── financial_data_agent.py
│   ├── news_sentiment_agent.py
│   ├── peer_comparison_agent.py
│   ├── fundamental_analysis_agent.py
│   ├── chart_generator_agent.py
│   └── summary_agent.py
├── tools/
│   ├── yfinance_tool.py
│   ├── newsapi_tool.py
│   ├── plotting_tool.py
│   └── export_tool.py
├── data/
│   └── transcripts/                # PDF earnings reports
├── fin_terms.py                    # Financial glossary definitions
├── utils.py                        # Common helper functions
├── main.py                         # Entry point (launch lead agent)
└── README.md



---

## 🧠 Future Improvements

| Feature                    | Description                                                   |
|----------------------------|---------------------------------------------------------------|
| 🧾 **RAG from Earnings PDFs** | Use OCR + LangChain to extract speaker-wise summaries     |
| 📂 **Portfolio Mode**          | Generate batch reports for multiple stock symbols         |
| 🖥️ **Frontend Integration**    | Build a React dashboard or Streamlit-based UI             |
| 📅 **Automated Scheduling**    | Auto-generate & email reports daily/weekly                |
| 📊 **CSV/Excel Export**        | Export financial tables in structured format              |
| 📈 **Enhanced Visuals**        | Add interactive charting (price/valuation/peer trends)    |

