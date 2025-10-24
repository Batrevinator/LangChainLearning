from langchain.tools import tool

import db_utils as db

@tool
def search(query: str) -> str:
    """ This tool searches the database for stores and products based on a given query.
    The query should be a valid PostgreSQL query string.
    Also make sure to include store names, product names, prices, and availability in your queries where relevant.
    The database schema is as follows:
    
    ----------
            
            Tables:

                stores
                Represents individual retail stores.
                Columns:

                store_id: integer, primary key. Unique ID for each store.

                name: text. Store name.

                location: text. Physical address or city of the store.

                phone_number: text. Optional store contact number.

                email: text. Optional contact email.

                website: text. Optional store website URL.

                products
                Represents global product entries.
                Columns:

                product_id: integer, primary key. Unique ID for each product.

                name: text. Product name.

                item_type: text. Broad product category such as Food, Cleaning, or Personal Care.

                store_products
                Represents the many-to-many relationship between stores and products. Each row indicates that a store sells a given product.
                Columns:

                store_id: integer, foreign key referencing stores.store_id.

                product_id: integer, foreign key referencing products.product_id.

                price: decimal. Store-specific product price.

                quantity_available: integer. Number of units available at that store.

                discount: decimal, representing a percentage between 0 and 100. Discount currently applied by that store for that product.
                Primary key: (store_id, product_id).

            Relationships:
                One store can sell many products.
                One product can be sold by many stores.
                The link between stores and products is managed through the store_products table.

            Usage Examples:
                To list all products sold by a store, join stores to store_products to products.
                To compare product prices across stores, join products to store_products to stores.
                To find discounted items, filter store_products where discount > 0.
                
            ----------

    Args:
        query (str): A PostgreSQL query string.

    Returns:
        str: The results of the query as a string.
    """
    store_info = db.exec_get_all(query)
    sql = "INSERT INTO PreviousQueries (query_text) VALUES (%s);"
    db.exec_commit(sql, (query,))
    # print(store_info)
    return str(store_info)

# I would like to figure out how to get the agent to ask the user questions when it needs more information.
# This does not seem to be the method...
# @tool
# def ask_user_question(question: str) -> str:
#     """ A tool to ask the user a question and get their input.

#     Args:
#         question (str): The question to ask the user.
#     Returns:
#         str: The user's input.
#     """
#     return input(question)


@tool
def route_distance_calculator(distances: list[float]) -> float:
    """ A tool to calculate the total distance of a route given a list of distances between locations.

    Args:
        distances (list[float]): A list of distances between locations.

    Returns:
        float: The total distance of the route.
    """
    return sum(distances)

def retrieve_prev_queries() -> str:
    sql: str = "SELECT * FROM PreviousQueries LIMIT 10;"
    prev_quries = db.exec_get_all(sql)
    return prev_quries