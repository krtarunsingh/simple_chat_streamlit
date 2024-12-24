import streamlit as st

# Set the title of the app
st.title("Simple Chat App")

# Initialize session state for messages
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Function to add user message and bot response


def send_message():
    user_input = st.session_state["user_input"]
    if user_input:
        # Add user message
        st.session_state['messages'].append(
            {"role": "user", "content": user_input})
        # Add bot response
        st.session_state['messages'].append(
            {"role": "bot", "content": "Hello World"})
        # Clear input box
        st.session_state["user_input"] = ""


# Display messages
for message in st.session_state['messages']:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Bot:** {message['content']}")

# Input box for user to type messages
st.text_input("You:", key="user_input", on_change=send_message)
