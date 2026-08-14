import uuid
from langchain_classic.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI


def create_new_chat(chats: dict) -> str:
    chat_id = str(uuid.uuid4())
    
    chats[chat_id] = {
        "title": "New Chat",
        "memory": ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
    }
    
    return chat_id


def generate_chat_title(user_message: str, api_key: str) -> str:
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-3.1-flash-lite",
            temperature=0.3,
            google_api_key=api_key,)

        prompt = f"""
Generate a short chat title with a maximum of 4 words.

Rules:
- Do not use quotes.
- Do not add punctuation at the end.
- Be concise and descriptive.

User message:
{user_message}

Title:
"""

        response = llm.invoke(prompt)

        # Get the text from Gemini's response
        if isinstance(response.content, list):
            title = "".join(
                item.get("text", "")
                for item in response.content
                if isinstance(item, dict)
            )
        else:
            title = response.content
        return title if title else "New Chat"

    except Exception as e:
        print(f"Title generation error: {e}")
        return "New Chat"
    

def update_chat_title(chats: dict, chat_id: str, new_title: str):
    if chat_id in chats:
        chats[chat_id]["title"] = new_title