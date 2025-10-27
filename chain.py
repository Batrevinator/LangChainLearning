import os
from dotenv import load_dotenv
import db_utils as db
from locationGraph import LocationGraph
from location import Location
import random
from model import OpenAIModel
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
import agentTools as tools

def main():
    
    # In actuallity this should be derrived from the DB but for simplicity we hardcode it here
    # Goal is to create a graph of locations (stores, homes, etc.) with distances between them
    # This should try to emulate real life where you may only be able to access certain locations from others
    # Create locations based on existing stores in the DB:

    graph = {} 

    HomeLocations = {
        Location("Home A", "123 Main St, Anytown, USA", "home"),
        Location("Home B", "456 Oak Ave, Sometown, USA", "home"),
        Location("Home C", "789 Pine Rd, Othertown, USA", "home"),
    }

    sql = """
    SELECT DISTINCT name, location FROM stores;
    """

    store_locations = db.exec_get_all(sql)

    for store in store_locations:
        name = store[0]
        address = store[1]
        newLocation: Location = Location(name, address, "store")
        graph[newLocation] = []
        
    graph.update({home: [] for home in HomeLocations})
        
    # For now we will randomly connect locations with distances
    # One downfall of this method is it may create locations that are not reachable from others.
    # This could create interesting situations for the agent to navigate, I would like to see how it handles them.
    # This system may also run into situations where there are two routes between locations with different distances.
    # While this is a little strange it does reflect real life scenarios. I would like to see how the agent handles this as well.
    for location in graph.keys():
        possible_neighbors: list[Location] = list(graph.keys())
        possible_neighbors.remove(location)
        num_neighbors: int = random.randint(1, min(2, len(possible_neighbors)))
        neighbors: list[Location] = random.sample(possible_neighbors, num_neighbors)
        for neighbor in neighbors:
            distance: int = random.uniform(1.0, 20.0)  # Random distance between 1 and 20 units
            location.addNeighbor(neighbor, distance)
            graph[location].append((neighbor, distance))
    
    newLocationGraph: LocationGraph = LocationGraph(graph)
    print(newLocationGraph.show_graph())
    
    # system_query = input("Please enter your shopping list or query: ")
    # prompt_template = ChatPromptTemplate.from_messages([
    #         ("system", f"""
    #         You are shopping assistant agent which helps people to find great deals on their shopping lists. 
    #         You will receive shopping lists or queries from users and then determine which major stores to go based on their requests.
    #         If the user does not indicate a preference for optimization, optimize for cheapest prices.
            
    #         If no previous queries are relevant, generate a new PostgreSQL query to retrieve the necessary information from the database to help the user with their shopping list and use the "search" tool to execute it.
            
    #         If when using the "search" tool you get an error related to SQL syntax, correct the query and try again.
    #         If when using the "search" tool you do not get any results, tell the user that no results were found for their query.
            
    #         If there is a query in the following list of previous queries that could provide pertinent information for the user's question, use that query instead of generating a new one.
            
    #         Previous Queries: 
    #         -----
    #         {tools.retrieve_prev_queries()}
    #         -----
            
    #         If the user should request information on how to navigate to different locations, use the following location graph to determine distances between locations:
    #         -----
    #         {newLocationGraph.show_graph()}
    #         -----
    #         There may be locations that are not reachable from others. If this occurs inform the user.
            
    #         If a user can benefit from visiting multiple stores to fulfill their shopping list, provide a route that minimizes total travel distance while considering store locations and distances between them.
    #         Use the "route_distance_calculator" tool to help calculate total distances for routes you generate.
    #     """),
    #     ])
    # queryAgent: OpenAIModel = OpenAIModel(
    #     sys_prompt = prompt_template.format(),
        
    #     model="openai:gpt-4o-mini",
    #     tools = [tools.search]
    # )
    
    # response = queryAgent.prompt_model(f"""
    #         Here is the user's shopping list or query:
    #         -----
    #         {system_query}
    #         -----
    #         """)
    # # Extract content from the final AIMessage in the messages list
    # from langchain_core.messages import AIMessage
    # final_message = [msg for msg in response['messages'] if isinstance(msg, AIMessage)][-1]
    # print(final_message.content)

    
    
if __name__ == "__main__":
    load_dotenv()
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_AI_API_KEY")
    main()