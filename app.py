import streamlit as st

from functions.chat_management import (
    create_new_chat,
    generate_chat_title,
    update_chat_title,
)

from functions.agents import create_agent_executor_for_chat


# -----------------------------
# Page settings
# -----------------------------

st.set_page_config(
    page_title="AI Agent with Tool Calling",
    page_icon="🤖",
    layout="wide",
)


# -----------------------------
# Session State
# -----------------------------

if "api_key" not in st.session_state:
    st.session_state.api_key = None

if "chats" not in st.session_state:
    st.session_state.chats = {}

if "active_chat_id" not in st.session_state:
    st.session_state.active_chat_id = create_new_chat(
        st.session_state.chats
    )


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("AI Agent with Tool Calling 🤖")

    st.link_button(
        label="Click here to get API key",
        url="https://aistudio.google.com/app/apikey",
        use_container_width=True
    )

    user_api_key = st.text_input(
        "Gemini API Key",
        type="password"
    )

    st.markdown(
        "Your API key is used only in this session and is not saved permanently."
    )

    submit_button = st.button("Enter")

    if submit_button:

        if user_api_key:
            st.session_state.api_key = user_api_key
            st.success("API Key added successfully")

        else:
            st.error("Please enter your Gemini API key")


    # New chat button

    if st.button(
        "New Chat",
        use_container_width=True
    ):

        new_chat_id = create_new_chat(
            st.session_state.chats
        )

        st.session_state.active_chat_id = new_chat_id

        st.rerun()


    st.divider()

    st.subheader("Chat History")


    # Display chats

    for chat_id, chat_data in st.session_state.chats.items():

        button_type = (
            "primary"
            if chat_id == st.session_state.active_chat_id
            else "secondary"
        )

        if st.button(
            chat_data["title"],
            key=f"chat_{chat_id}",
            use_container_width=True,
            type=button_type
        ):

            st.session_state.active_chat_id = chat_id

            st.rerun()


# -----------------------------
# Main Page
# -----------------------------

st.title("AI Agent with Tool Calling")

st.markdown(
    "🚀 A Streamlit chatbot powered by Gemini with tool calling support"
)


# -----------------------------
# Active Chat
# -----------------------------

active_chat = st.session_state.chats[
    st.session_state.active_chat_id
]


# -----------------------------
# Display Old Messages
# -----------------------------

messages = active_chat["memory"].chat_memory.messages


for message in messages:

    role = (
        "user"
        if message.type == "human"
        else "assistant"
    )

    with st.chat_message(role):
        st.markdown(message.content)


# -----------------------------
# User Input
# -----------------------------

prompt = st.chat_input("Ask me anything...")


if prompt:

    # Check API key first

    if not st.session_state.api_key:

        st.error(
            "Please enter your Gemini API key first."
        )

        st.stop()


    # Display user message

    with st.chat_message("user"):
        st.markdown(prompt)


    # Generate title only for new chat

    if active_chat["title"] == "New Chat":

        try:

            title = generate_chat_title(
                prompt,
                st.session_state.api_key
            )

            update_chat_title(
                st.session_state.chats,
                st.session_state.active_chat_id,
                title
            )

        except Exception as error:

            print(
                f"Title generation error: {error}"
            )


    # Run the agent

    try:

        with st.chat_message("assistant"):

            with st.spinner("🤔 Thinking..."):

                # Create the agent for this chat
                agent_executor = create_agent_executor_for_chat(
                    active_chat["memory"],
                    st.session_state.api_key
                )

                # Get previous messages
                chat_history = (
                    active_chat["memory"]
                    .chat_memory
                    .messages
                )

                # Send previous messages and the new message
                result = agent_executor.invoke(
                    {
                        "messages": chat_history + [
                            ("user", prompt)
                        ]
                    }
                )

                # Get the final assistant response
                response = result["messages"][-1].content


                # Convert Gemini structured output
                # into normal text
                if isinstance(response, list):

                    response = "".join(
                        item.get("text", "")
                        for item in response
                        if isinstance(item, dict)
                    )


                # Save user message
                active_chat["memory"].chat_memory.add_user_message(
                    prompt
                )


                # Save assistant message
                active_chat["memory"].chat_memory.add_ai_message(
                    response
                )


            # Display response
            st.markdown(response)


        # Refresh the page so the new title
        # and messages appear
        st.rerun()


    except Exception as error:

        st.error(
            f"{type(error).__name__}: {error}"
        )