from langchain.agents import create_agent
from langchain.tools import tool

from langchain_openai import ChatOpenAI
import os

class OpenAIModel:
    
    def __init__(self, sys_prompt: str, model: str, tools: list = []):
        # self.llm = ChatOpenAI(model_name=self.model, 
        #                       temperature=temperature, 
        #                       max_tokens = 100, 
        #                       timeout = 30, 
        #                       api_key=os.getenv("OPEN_AI_API_KEY"))
        self.agent = create_agent(
            model=model,
            tools=tools,
            system_prompt=sys_prompt
        )
        
    def prompt_model(self, prompt: str) -> str:
        return self.agent.invoke({"messages": [{"role": "user", "content": prompt}]})