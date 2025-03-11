import streamlit as st
import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType
from langchain.prompts import MessagesPlaceholder

from tool import get_latest_videos

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="MixiBot")
st.title("MixiBot")

msgs = StreamlitChatMessageHistory(key="langchain_messages")
memory = ConversationBufferMemory(chat_memory=msgs, return_messages=True)

if len(msgs.messages) == 0:
    msgs.add_ai_message("Xin chào. Tôi là một chatbot thông minh.")

llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo', openai_api_key=openai_api_key)
open_ai_agent = initialize_agent(
    llm=llm,
    tools=[get_latest_videos],
    agent=AgentType.OPENAI_FUNCTIONS,
    agent_kwargs={
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="history")]
    },
    verbose=True,
    memory=memory
)

for msg in msgs.messages:
    st.chat_message(msg.type).write(msg.content)

if prompt := st.chat_input(disabled=not openai_api_key):
    st.chat_message("human").write(prompt)
    with st.spinner("Đang suy nghĩ ..."):
        response = open_ai_agent.run(prompt)
        st.chat_message("ai").write(response)