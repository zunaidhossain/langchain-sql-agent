from config import llm
from prompts import SYSTEM_PROMPT
from tools import execute_sql
from langchain.agents import create_agent

agent = create_agent(
    model=llm,
    tools=[execute_sql],
    system_prompt=SYSTEM_PROMPT
)