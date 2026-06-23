from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from tools import calculator, word_counter

# Load API KEY
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Gemini Model
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash",
    google_api_key = GOOGLE_API_KEY,
    temperature = 0)

# Tools
tools = [calculator, word_counter]

# Prompt
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant that can use tools."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

prompt = ChatPromptTemplate. from_messages(
    [
        ("system",
        "You are a helpful AI Assistant. \n"
        "You can answer questions using your own knowledge. \n"
        "Use tools only when necessary. \n"
        "If a question requires calculation, use the calculator tool. \n"
         "If a question asks for word count, use the word_counter tool"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ]
)

## Create agent
agent = create_tool_calling_agent(
    llm,
    tools,
    prompt)

# Create agent
agent = create_tool_calling_agent(
    
    llm,
    tools,
    prompt
)

# Agent executer
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True)

def my_output(query) -> Any:
    result = agent_executor.invoke({"input": query})
    return result["output"]

# UI
st.set_page_config(page_title="AI Agent")
st.title("Gemini Agent Bot")
query = st.text_input("Ask me anything:")
if st.button("Ask Agent"):
    response = my_output(query)
    st.subheader("Response")
    st.write(response)