import os
import sys
from dotenv import load_dotenv
import json
import db_utils as db
from model import OpenAIModel
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
import agentTools as tools

def main():
    
    system_query = input("Please enter your shopping list or query: ")
    prompt_template = ChatPromptTemplate.from_messages([
            ("system", f"""
            You are shopping assistant agent which helps people to find great deals on their shopping lists. 
            You will receive shopping lists from users and then determine which major stores to go to for best prices for each item on those lists.
            If there is a query in the following list of previous queries that could provide pertinent information for the user's question, return that query instead of generating a new one.
            Previous Queries: 
            -----
            {tools.retrieve_prev_queries()}
            -----
            
            If no previous queries are relevant, generate a new PostgreSQL query to retrieve the necessary information from the database to help the user with their shopping list and use the "search" tool to execute it.
            If when using the "search" tool you get an error related to SQL syntax, correct the query and try again.
            If when using the "search" tool you do not get any results, tell the user that no results were found for their query.
        """),
        ])
    queryAgent: OpenAIModel = OpenAIModel(
        sys_prompt = prompt_template.format(),
        
        model="openai:gpt-4o-mini",
        tools = [tools.search]
    )
    
    response = queryAgent.prompt_model(f"""
            Here is the user's shopping list or query:
            -----
            {system_query}
            -----
            """)
    # Extract content from the final AIMessage in the messages list
    from langchain_core.messages import AIMessage
    final_message = [msg for msg in response['messages'] if isinstance(msg, AIMessage)][-1]
    print(final_message.content)

    
    
if __name__ == "__main__":
    load_dotenv()
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_AI_API_KEY")
    main()