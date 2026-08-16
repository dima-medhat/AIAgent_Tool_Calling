[README.md](https://github.com/user-attachments/files/31120450/README.md)
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


---

## 🎯 Overview

This project is an **AI Agent** capable of using external tools to solve user requests. Unlike a standard chatbot that relies only on its training data, this agent can:

- **Calculate** mathematical expressions with precision
- **Search the web** for current information and news
- **Check weather** in real-time for any city

The agent **automatically decides** which tool to use (or if no tool is needed) based on the user's question.

---

## 🎯 Objectives

- Implement t three tools: Calculator, Weather, and Search
-  Allow the agent to automatically select the appropriate tool
-  Build a conversational UI with chat history
-  Support multiple chat sessions with auto-generated titles
-  Use in-memory conversation history for context awareness

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
| **Google Gemini** | Large Language Model (the brain) |
| **Streamlit** | Web-based user interface |
| **DuckDuckGo Search** | Free web search API |
| **Weather tool** | Free weather API |
| **python-dotenv** | Environment variable management |

---

## 📦 Installation

### Prerequisites

- Python 3.10 or higher

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
AIAgent_Tool_Calling/
|
├── tools/                          
│   ├── __init__.py
│   ├── calculator.py              
│   ├── search_tool.py             
│   └── weather_tool.py             
│
├── functions/                      
│   ├── __init__.py
│   ├── chat_management.py          
│   └── agents.py
|
|__ images/
|   |__ Tool_Calling_Chatbot.png
|   |__ Tool_Calling_Chatbot_Home.png      
│
├── app.py                         
├── requirements.txt                
├── .env                   
├── .gitignore                      
├── README.md
|__ test_gemini.py
|__ test_model.py                         

```

## 📸 Screenshots

### 2. Chat Interface
![Chat Interface](images/Tool_Calling_Chatbot_home.png)

### 3. Tool in Action
![Tool Calling](images/Tool_Calling_Chatbot.png)

---

## 📄 File Descriptions

| File | What It Does |
|------|-------------|
| `tools/calculator.py` | Safe math evaluation with character whitelist and restricted `eval()` |
| `tools/search_tool.py` | Web search using DuckDuckGo — no API key required |
| `tools/weather_tool.py` | Weather lookup   |
| `functions/chat_management.py` | Creates new chats, generates titles using Gemini, updates titles |
| `functions/agents.py` | Builds the `AgentExecutor` with given memory and API key |
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


---

## 🙏 Acknowledgments

- [LangChain](https://www.langchain.com/) for the agent framework
- [Google AI Studio](https://aistudio.google.com/) for the Gemini API
- [Streamlit](https://streamlit.io/) for the easy-to-use UI framework

---

