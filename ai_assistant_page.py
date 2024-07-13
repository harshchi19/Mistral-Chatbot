import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to clear chat history
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Function to generate AI assistant response
def generate_insurance_assistant_response(prompt_input, client):
    system_message = "You are a consultant with expertise in personal finance and insurance. Provide crisp and short responses."

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt_input}
    ]

    response = ""
    for message in client.chat_completion(
            messages=messages,
            max_tokens=120,
            stream=True
    ):
        response += message.choices[0].delta.content or ""

    return response

# Define the AI Assistant page
def ai_assistant_page():
    st.title('AI Assistant')
    st.write("Your personal insurance and finance expert")

    # Custom CSS for chat containers
    st.markdown("""
    <style>
    .user-container {
        background-color: #2b5c8a;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
    .assistant-container {
        background-color: #1e3d5a;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
    .chat-text {
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

    # Define sidebar for AI Assistant configurations
    with st.sidebar:
        st.title('🏛️🔍 AI-Assistant Settings')
        hf_api_token = "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"
        if hf_api_token:
            st.success('API key loaded from environment variable!', icon='✅')
        else:
            st.error('API key not found. Please set the HUGGINGFACE_API_TOKEN environment variable.', icon='🚨')

        # Initialize the InferenceClient
        client = InferenceClient(
            "mistralai/Mixtral-8x7B-Instruct-v0.1",
            token=hf_api_token
        )

        st.button('Clear Chat History', on_click=clear_chat_history)

    # Initialize session state for messages
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

    # Display chat history
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            container_class = "user-container" if message['role'] == "user" else "assistant-container"
            st.markdown(f"""
            <div class="{container_class}">
                <p class="chat-text"><strong>{'You' if message['role'] == 'user' else 'Assistant'}:</strong> {message['content']}</p>
            </div>
            """, unsafe_allow_html=True)

    # Handle user input and generate responses
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_input("Type your message here:", key="user_input")
        submit_button = st.form_submit_button("Send")

    if submit_button and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = generate_insurance_assistant_response(user_input, client)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.experimental_rerun()

# Run the app
if __name__ == "__main__":
    ai_assistant_page()
