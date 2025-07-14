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


| Layer                   | Tools/Technologies                                                  |
| ----------------------- | ------------------------------------------------------------------- |
| **Data Fetching**       | `yfinance`, `NewsAPI`, `Yahoo Finance API`                          |
| **LLM / Reasoning**     | `OpenAI GPT-4o`, `LangChain`                                        |
| **Agent Orchestration** | `LangChain Agents`, `LangGraph` *(optional)*, `CrewAI` *(optional)* |
| **Visualization**       | `matplotlib`, `seaborn`, `plotly`                                   |
| **Export**              | `fpdf`, `jinja2`, `pdfkit` *(optional)*                             |
| **RAG (Optional)**      | `LangChain + Pinecone + OCR` *(for transcripts)*                    |
