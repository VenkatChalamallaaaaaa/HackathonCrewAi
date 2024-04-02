from crewai import Agent, Crew, Process, Task
from langchain_community.tools import DuckDuckGoSearchRun
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os


llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyCApXbTlB1M2k-L9S-LLWzp5xXD3VZleJM")

search_tool = DuckDuckGoSearchRun()

st.title('Research & Write')

topic = st.text_input('Topic')



result = crew.kickoff()
st.write(result)


