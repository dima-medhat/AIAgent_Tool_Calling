# 🤖 AI Agent with Tool Calling

> An intelligent assistant that autonomously decides when to use external tools — built with **LangChain**, **Google Gemini**, and **Streamlit**.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Objectives](#-objectives)
- [Features](#-features)
- [Technologies](#-technologies)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [File Descriptions](#-file-descriptions)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 🎯 Overview

This project is an **AI Agent** capable of using external tools to solve user requests. Unlike a standard chatbot that relies only on its training data, this agent can:

- **Calculate** mathematical expressions with precision
- **Search the web** for current information and news
- **Check weather** in real-time for any city

The agent **automatically decides** which tool to use (or if no tool is needed) based on the user's question.

---

## 🎯 Objectives

- [x] Implement at least three tools: Calculator, Weather, and Search
- [x] Allow the agent to automatically select the appropriate tool
- [x] Build a conversational UI with chat history
- [x] Support multiple chat sessions with auto-generated titles
- [x] Use in-memory conversation history for context awareness

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔢 **Calculator Tool** | Evaluates math expressions safely using restricted `eval()` |
| 🌤️ **Weather Tool** | Fetches real-time weather data via wttr.in (no API key needed) |
| 🌐 **Web Search Tool** | Searches DuckDuckGo for current news and facts (no API key needed) |
| 🧠 **Auto Tool Selection** | Gemini decides which tool to call — or answers directly |
| 💬 **Chat History** | Remembers context within a conversation |
| 📝 **Auto Titles** | Generates chat titles from the first user message |
| 🔄 **Multiple Chats** | Create and switch between independent conversations |
| 🔑 **API Key Input** | User enters their own Gemini API key in the UI |

---

## 🛠️ Technologies

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **LangChain** | Agent orchestration and tool management |
| **Google Gemini 2.5 Flash** | Large Language Model (the brain) |
| **Streamlit** | Web-based user interface |
| **DuckDuckGo Search** | Free web search API |
| **wttr.in** | Free weather API |
| **python-dotenv** | Environment variable management |

---

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- A free Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/ai-agent-tool-calling.git
cd ai-agent-tool-calling
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv

:: Windows
venv\Scripts\activate

:: macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### First Time Setup

1. Open the app in your browser
2. Enter your **Gemini API Key** in the sidebar
3. Click **Enter**
4. Start chatting!

### Example Questions to Try

| Question | Expected Tool Used |
|----------|-------------------|
| *"What is 15% of 240?"* | Calculator |
| *"What's the weather in Tokyo?"* | Weather |
| *"Latest news about AI"* | Web Search |
| *"Tell me a joke"* | None (direct answer) |
| *"What's the temperature in London plus 10 degrees?"* | Weather + Calculator |

---

## 📁 Project Structure

```
AI_Agent_w_ToolCalling/
|
├── tools/                          # External capabilities
│   ├── __init__.py
│   ├── calculator.py               # Math evaluation tool
│   ├── search_tool.py              # DuckDuckGo web search
│   └── weather_tool.py             # wttr.in weather lookup
│
├── functions/                      # Core logic
│   ├── __init__.py
│   ├── chat_management.py          # Chat creation & title generation
│   └── agent_builder.py            # Agent + memory builder
│
├── app.py                          # Streamlit UI
├── requirements.txt                # Python dependencies
├── .env.example                    # API key template
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
└── architecture_diagram.png        # System architecture
```

---

## 📸 Screenshots

> _Add your screenshots here after running the app_

### 1. API Key Setup
![API Key Setup](screenshots/api_key_setup.png)

### 2. Chat Interface
![Chat Interface](screenshots/chat_interface.png)

### 3. Tool in Action
![Tool Calling](screenshots/tool_calling.png)

---

## 📄 File Descriptions

| File | What It Does |
|------|-------------|
| `tools/calculator.py` | Safe math evaluation with character whitelist and restricted `eval()` |
| `tools/search_tool.py` | Web search using DuckDuckGo — no API key required |
| `tools/weather_tool.py` | Weather lookup using wttr.in — no API key required |
| `functions/chat_management.py` | Creates new chats, generates titles using Gemini, updates titles |
| `functions/agent_builder.py` | Builds the `AgentExecutor` with given memory and API key |
| `app.py` | Streamlit frontend — sidebar, chat history, message display, input handling |
| `requirements.txt` | All Python packages needed to run the project |

---

## 🔮 Future Improvements

As a student project, here are areas for future enhancement:

| Improvement | Description |
|-------------|-------------|
| **Persistent Storage** | Save chat history to a database (SQLite/PostgreSQL) instead of memory |
| **More Tools** | Add tools like: current time, currency converter, file reader |
| **Better Error Handling** | Show user-friendly messages when tools fail |
| **Export Chats** | Allow users to download conversation history as PDF or text |
| **Dark Mode** | Add theme switching in Streamlit |
| **Voice Input** | Add speech-to-text for hands-free interaction |
| **Tool Call Visualization** | Show in the UI which tool was called and what it returned |

---

## 👤 Author

**Your Name**
Computer Engineering Student

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)

---

## 🙏 Acknowledgments

- [LangChain](https://www.langchain.com/) for the agent framework
- [Google AI Studio](https://aistudio.google.com/) for the Gemini API
- [Streamlit](https://streamlit.io/) for the easy-to-use UI framework

---

> _This project was built as part of an AI Agent with Tool Calling assignment._
